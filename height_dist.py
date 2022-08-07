import matplotlib.pyplot as plt
from vis_rigis_data import lognormal_, dispersion, expection
import numpy as np
from scipy.stats import lognorm

def height_dist(data, _div = 10):
    data_e_0 = [i for i in data if i != 0]
    min_h = min(data)/2
    max_h = max(data)*2+0.01
    delta = max_h - min_h
    step = delta / _div
    counter = 0
    x = [min_h + step / 2 + i * step for i in range(_div)]
    y = [0 for i in range(_div)]
    for i in data:
        index = (i - min_h)//step
        y[int(index)] += 1
    fig, ax = plt.subplots()
    #ax.scatter(0, len([i for i in data if i == 0])/len(data))
    e = expection(data_e_0)
    print("e = ", e)
    d = np.sqrt(dispersion(data_e_0, e))
    
    #ax.plot(x, lognorm(d).pdf(x))
    print("d = ", d)
    ax.plot(x, lognormal_(x, e, d), 'r-', lw=5, alpha=0.6, label='lognorm pdf')
 #  ax.scatter(x,y)
    plt.show()

hs = list(map(float,np.load("heights.npy", 'r')))
height_dist(hs, 10500)
