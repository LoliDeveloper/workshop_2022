import lasio
import sys
import numpy as np
import matplotlib.pyplot as plt
import math 

k_por = []

for arg in sys.argv[1::]:
    las = lasio.read(arg)
    Keys=las.keys()
    print(Keys)
    'DEPT', 'NAS_T', 'LIT_T', 'KP_T', 'KG_T', 'KPR_T:1', 'KPR_T:2'
    nas= las['NAS_T']
    dept= las['DEPT']
    lit = las['LIT_T']
    kp = las['KP_T']
    
    for k in kp:
        if not (math.isnan(k)): 
            k_por.append(k)
    kg=las['KG_T']
    kpr1=las['KPR_T:1']
    kpr2=las['KPR_T:2']
#визуализация кривых лас-файла

    fig, ax1 = plt.subplots(figsize=(12, 4))
    fig.suptitle(arg)
    fig.canvas.set_window_title(arg)
    color = 'tab:red'
    ax1.set_xlabel("Depth, m")
    ax1.set_ylabel("Тип насыщения, gAPI", color=color)
    ax1.plot(dept, nas, color=color, label=str(Keys[1]))
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx() 

    color = 'tab:blue'
    ax2.set_ylabel("Литология (песок/глина), m3/m3", color=color)
    ax2.plot(dept, lit, color=color, label=u'LIT_T')
    ax2.tick_params(axis='y', labelcolor=color)

    ax3 = ax1.twinx() 


    color = 'tab:green'
    ax3.set_ylabel("Koef poristost, us/ft", color=color)
    ax3.plot(dept, kp, color=color ,label=u'KP_T')
    ax3.tick_params(axis='y',size=12, labelcolor=color, pad=80)

    ax4 = ax1.twinx()


    color = 'tab:purple'
    ax4.set_ylabel("Koef gazonasish, us/ft", color=color)
    ax4.plot(dept, kg, color=color ,label=u'Kg')
    ax4.tick_params(axis='y',size=12, labelcolor=color, pad=120)

    ax5 = ax1.twinx()

    color = 'tab:orange'
    ax5.set_ylabel("Koef pronits, us/ft", color=color)
    ax5.plot(dept, kpr1, color=color ,label=u'Kpr1')
    ax5.tick_params(axis='y',size=12, labelcolor=color, pad=160)

    plt.grid(True)
    plt.legend(loc='upper right')

    fig.tight_layout() 
#сохранение изображения
    fig.savefig(arg.split('/')[-1]+'.png', dpi=200, orientation='landscape')
    #plt.show()
print(k_por)
