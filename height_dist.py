import matplotlib.pyplot as plt
from vis_rigis_data import normal_, dispersion, expection
import numpy as np

def draw_height_dist(data, _div = 10):
    data_e_0 = [i for i in data if i != 0]
    min_h = min(data_e_0)
    max_h = max(data)+0.01
    delta = max_h - min_h
    step = delta / _div
    counter = 0
    x = [min_h + step / 2 + i * step for i in range(_div)]
    y = [0 for i in range(_div)]
    for i in data:
        index = (i - min_h)//step
        y[int(index)] += 1
    fig, ax = plt.subplots()
    ax.scatter(0, len([i for i in data if i == 0])/len(data))
    e = expection(data_e_0)
    d = dispersion(data_e_0, e)
    med_sq = sum([(i-normal_([i],e,d)[0])**2 for i in data_e_0])/len(data_e_0)
    print(np.sqrt(med_sq))
    ax.plot(x, normal_(x,e,d))
    ax.scatter(x,y)
    plt.show()

hs = list(map(float,np.load("heights.npy", 'r')))
draw_height_dist(hs)
