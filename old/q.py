from height_dist import height_dist
import random

_div = 100

hs = list(map(float,np.load("heights.npy", 'r')))

count_0 = len([x for x in hs if x == 0])

max_height = max(hs)
min_height = min(hs)
delta_height = max_height - min_height

rd_h = []
for i in range(_div):
    
    if(random.uniform(0.1) > )
    rd_h.append(min_height + random.uniform(0,1)*delta_height)


kps = list(map(float,np.load("k_pors.npy",'r')))

max_kps = max(kps)
min_kps = min(kps)
delta_kps = max_kps - min_kps

kns = list(map(float, np.load("k_nas.npy",'r')))

max_kns = max(kns)
min_kns = min(kns)
delta_kns = max_kns - min_kns

draw_height_dist(hs)


