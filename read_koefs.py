import lasio
import sys
import numpy as np
import matplotlib.pyplot as plt
import math 

k_por = []
k_nas = []
if len(sys.argv[1::]) < 1:
    print("Введите аргументы(файлы .las)")
    return
for arg in sys.argv[1::]:
    las = lasio.read(arg)
    Keys=las.keys()
    print(Keys)
    'DEPT', 'NAS_T', 'LIT_T', 'KP_T', 'KG_T', 'KPR_T:1', 'KPR_T:2'
    nas= las['NAS_T']
    dept= las['DEPT']
    lit = las['LIT_T']
    kp = las['KP_T']
    kgt = las['KG_T']
    for k in kp:
        if not (math.isnan(k)): 
            k_por.append(k)
    
    for k in kgt:
        print(k)
        if not (math.isnan(k)):
            k_nas.append(k)
np.save("k_pors", k_por)
np.save("k_nas", k_nas)
print(k_nas)
