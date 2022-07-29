import numpy as np
import math

kgn = np.load("k_nas.npy", 'r')

def find_tuple(gaznas):
    puc = []
    for i in range(len(gaznas)):
        if (not (math.isnan(gaznas[i]))):
            puc.append([dept[i],gaznas[i]])
    return puc

height_gaz = find_tuple(kgn)
h = []

for temp in  height_gaz:
    if len(temp)!=0 :
        h.append(temp[-1][0]-temp[0][0])
    else:
        h.append(0)
print(h)
