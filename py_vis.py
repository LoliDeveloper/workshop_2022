import numpy as np
from matplotlib import pyplot as plt
import math
k_nas = np.load("k_nas.npy", 'r')
k_por = np.load("k_pors.npy",'r')

def normal_():


def dispersion(data = [], expection=0):
    _sum = 0
    for i in data:
        _sum+=(expection - i)**2
    return _sum/len(data)


def expection(data = []):
    return sum(data)/len(data)


def visualize_data(data = [], _div = 5, x_label = 'x_label', y_label = 'y_label'):
    data_count = [0 for x in range(_div)]

    max_data = max(data)+0.01
    min_data = min(data)
    delta = max_data - min_data

    step = delta/_div
    steps = [min_data+step/2]
    for i in range(1,_div):
        steps.append(steps[-1]+step)
    for k in data:
        index = (k - min_data)/step
        data_count[int(index)]+=1
    print(data_count)

    fig, ax = plt.subplots(layout='constrained')
    fig.suptitle('_div = '+str(_div))
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    fig.tight_layout();
    ax.plot(steps, data_count)
    x = np.linspace(0,2,100)

#ax.plot(x,1/(2*np.sqrt(np.pi))*np.exp(-1/2*(x**2)), 'Нормальное распределение')
    plt.show()

visualize_data(k_nas, 50, "Коэф насыщенности", "кол-во скважин")
visualize_data(k_por, 10, "Коэф пористости", "кол-во скважин")
