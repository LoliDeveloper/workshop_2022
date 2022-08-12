# %%
import numpy as np
from matplotlib import pyplot as plt
import math
import lasio
import os
import pandas as pd
path_to_RIGIS = r'./welldata/RIGIS/'
path_to_GIS = r'./welldata/GIS_md/'
path_to_welltracks = r'./welldata/welltracks.txt'

def getLasDataFrames(path = path_to_RIGIS):
    lasDF = []
    lasFileNames = []
    for file in os.listdir(path):
        if file.endswith('.las'):
            lasFileNames.append(file[:-4])
            lasDF.append(lasio.read(path+file).df())
    return (lasDF, lasFileNames)

lasDataFrame, lasFileNames = getLasDataFrames()

# %%
len(lasDataFrame)

# %%
def parse_welltracks():
    welltracks = []
    f = open(path_to_welltracks)
    welldata = f.read().split(';')
    for well in welldata:
        if len(well.split()) > 2:
            name = well.split()[2][:-1]
            data = well.split()[3:]
            x = [float(data[i]) for i in range(len(data)) if i % 4 == 0]
            y = [float(data[i]) for i in range(len(data)) if i % 4 == 1]
            tvdss = [float(data[i]) for i in range(len(data)) if i % 4 == 2]
            md = [float(data[i]) for i in range(len(data)) if i % 4 == 3]
            if(lasFileNames.count(name) > 0):
                welltracks.append([name, x, y ,tvdss, md]) # в таком виде хранятся
            else:
                print(name)

    return welltracks


# %%
from scipy.interpolate import interp1d
import math
def get_heights_list():
    welltracks = parse_welltracks()
    tvdconv = []
    for tracknum in range(len(welltracks)):
        f = interp1d(welltracks[tracknum][4], welltracks[tracknum][3])
        tvdconv.append(f)

    heights = []
    print(len(lasDataFrame))
    for k  in range(len(lasDataFrame)):
        frame = lasDataFrame[k]
        tmp_sum = 0
        for i in range(len(frame['KG_T']) - 1):
            if (frame['KG_T'].array[i + 1] >= 0):
                tmp_sum += tvdconv[k](frame['KG_T'].index[i + 1]) - tvdconv[k](frame['KG_T'].index[i])
        heights.append(tmp_sum)
    return heights
get_heights_list()

# %%
def get_k_nas_por():
    k_nas = []
    k_por = []
    for k in range(len(lasDataFrame)):
        frame = lasDataFrame[k]
        k_nas.append([val for val in frame['KG_T']])
        for k_w in range(len(k_nas)):
            for k in range(len(k_nas[k_w])):
                if math.isnan(k_nas[k_w][k]):
                    k_nas[k_w][k] = 0
        k_por.append([val for val in frame['KP_T']])

        for k_w in range(len(k_por)):
            for k in range(len(k_por[k_w])):
                if math.isnan(k_por[k_w][k]):
                    k_por[k_w][k] = 0
    return (k_nas, k_por)
k_nas,k_por = get_k_nas_por()

# %%
def dist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)
    
def perimeter(boundary):
    (prev_x,prev_y) = boundary[-1]
    perim = 0
    for (x,y) in boundary:
        perim += dist(x,y,prev_x,prev_y)
        prev_x, prev_y = x,y
    return perim
def getCommonLength(boundary1, boundary2):
    first_pt = -1
    second_pt = -1
    for i in range(int(boundary1.size/2 - 1)):
        for j in range(int(boundary2.size/2 - 1)):
            (x1, y1) = boundary1[i]
            (x2, y2) = boundary2[j]
            if(x1 == x2 and y1 == y2):
                if first_pt == -1:
                    first_pt = (x1,y1)
                else:
                    second_pt = (x2, y2)
                    return dist(first_pt[0],first_pt[1],second_pt[0],second_pt[1])
    return 0
    


# %%
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import contextily as ctx
from shapely import geometry
from shapely.ops import cascaded_union
from geovoronoi.plotting import subplot_for_map, plot_voronoi_polys_with_points_in_area
from geovoronoi import voronoi_regions_from_coords, points_to_coords

welltracks = parse_welltracks()
print('len(welltrack) = ', len(welltracks))
boundary = np.load("boundary.npy",'r') 

c = np.array([(track[1][0], track[2][0]) for track in welltracks])
s = geometry.Polygon(boundary)
main_area = s.area
region_polys, region_pts = voronoi_regions_from_coords(c, s)
perimeters = []
boundaries = []
new_polys = []
print('len(region_polys) = ', len(region_polys))
for i in range(len(region_polys)):
    #print(type(region_polys[i]))
    try:
        new_polys.append(region_polys[i])
        perimeters.append(perimeter(np.array(region_polys[i].boundary)))
        boundaries.append(region_polys[i].boundary)
    except Exception as e:
        perimeters.append(perimeter(np.array(list(region_polys[i])[0].boundary)))
        boundaries.append(list(region_polys[i])[0].boundary)


# %%
len(boundaries)

# %%

#print(perimeters)
fig, ax = subplot_for_map(figsize=(15, 9), dpi=400)
print("len(welltracks) = ", len(welltracks))
for i in range(len(welltracks)):
    ax.annotate(welltracks[i][0], (welltracks[i][1][0], welltracks[i][2][0]), fontsize=7)
plot_voronoi_polys_with_points_in_area(ax, s, region_polys, c, region_pts)
plt.show()


# %%

mat_size = len(welltracks)
print('mat size is ', mat_size)
adj_mat = [np.array([-1 for i in range(mat_size)]) for j in range(mat_size)]
for i in range(mat_size - 1):
    for j in range(mat_size - 1):
        for reg1 in region_pts[i]:
            for reg2 in region_pts[j]:
                if (i == j):
                    adj_mat[reg1][reg2] = 0
                    continue
                adj_mat[reg1][reg2] = getCommonLength(np.array(boundaries[i]), np.array(boundaries[j]))
                if(adj_mat[reg1][reg2] > 0):
                    print(reg1, ' and ', reg2, ' are neibors with common length ', adj_mat[reg1][reg2])
print(adj_mat)

# %%
squares = []
from main import parse_welltracks
for i in range(len(region_polys)):
    squares.append(region_polys[i].area)

# %%
bg = 0.00848016
def zero_formula(S, H, kp, kg, bg = 0.00848016, ft = 1, fp = 1):
    return S*H*kp*kg/bg


# %%

mean_k_nas = [sum(k)/len(k) for k in k_nas if len(k) > 0]
mean_k_por = [sum(k)/len(k) for k in k_por if len(k) > 0]
heights = get_heights_list()
print(heights)
print('mean k nas',mean_k_nas[0])
print('mean k por',mean_k_por[0])
print(k_nas[0], k_por[0])

# %%
from vis_rigis_data import visualize_data
print("zero_formula = ", zero_formula(main_area, sum(heights)/len(heights), sum(mean_k_por)/len(mean_k_por), sum(mean_k_nas)/len(mean_k_nas)))
visualize_data(heights, 6)
print("k_por med = ", mean_k_por[0])
print("k_nas med = ", mean_k_nas[0])
#plt.plot(,[])

# %%
len([np.mean(x) for x in k_nas])

# %%
from get_value import get_value

print(len(mean_k_nas), len(mean_k_por), len(heights), len(squares), len(adj_mat), len(perimeters))

v1 = get_value(mean_k_nas, mean_k_por, heights, squares, adj_mat, perimeters)
sum(v1)/bg

# %%
def get_value(k_gas,k_por,h,S,mat,P):
    value = []
    temp_value = []
    for i in range(len(k_gas)):
        temp_value.append(k_gas[i]*k_por[i]*h[i]/2)
        value.append(k_gas[i]*k_por[i]*h[i]/2)
    for i in range(len(k_gas)):
        for V in range(len(mat[i])):
            if mat[i][V]>0:
                value[i]+=mat[i][V]/P[i]*temp_value[V]
    value=[S[i]*x for x in value]
    return value


# In[181]:


def get_value2(k_gas,k_por,h,S,mat,P,compress = 100000):
    '''Считаем произведение вероятностей. Каждое значение перемножается с каждым другим. Перемножаем k_por k_gas h'''
    gas_por = []
    for i in range (len(k_gas)):
        
        temp = []
        for gas in k_gas[i]:
            for por in k_por[i]:
                temp.append(gas*por)
                
        gas_por_h = []
        for gaspor in temp:
            for H in h[i]:
                gas_por_h.append(gaspor*H/2)
                
        gas_por.append(gas_por_h)    
    for id_well in range (len(k_gas)):
        adskoe_raspredelenie=[]
        save = gas_por[id_well]
        for id_p_j in range(len(mat[id_well])):
            temp = []
            if (id_p_j!= id_well and mat[id_well][id_p_j]>0):
                for V in save:
                    for V_j in gas_por[id_p_j]:
                        temp.append(V+V_j*mat[id_well][id_p_j]/P[id_well])
                save = temp
            save = [x*S[id_well] for x in save]
            if len(save)>compress:
                save=honey_compress(save)
            adskoe_raspredelenie.append(save)
    return adskoe_raspredelenie


# In[174]:


def honey_compress(value_list, razmer_zhim=10000):
    value= len(value_list)
    temp_div= 2
    min_div = 1
    while(value>razmer_zhim):
        if (value%temp_div==0):
            min_div*=temp_div
            value= value//temp_div
        else:
            temp_div+=1
    value_list.sort();
    new_value_list=[sum(value_list[(x)*min_div:(x+1)*min_div])/min_div for x in range(value-1)]
    return new_value_list


# %%
#v2 = get_value2(k_nas, k_por, [[h] for h in heights], squares, adj_mat, perimeters, 10000000)

# %%



