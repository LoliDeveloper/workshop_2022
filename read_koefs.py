import lasio
import sys
import numpy as np
import matplotlib.pyplot as plt
import math 

def read_RIGIS():
    k_por = []
    k_nas = []
    ar_dept = []
    if len(sys.argv[1::]) < 1:
        print("Введите аргументы(файлы .las)")
    else:
        for arg in sys.argv[1::]:
            las = lasio.read(arg)
            Keys=las.keys()
            print(Keys)
    #    'DEPT', 'NAS_T', 'LIT_T', 'KP_T', 'KG_T', 'KPR_T:1', 'KPR_T:2'
            nas= las['NAS_T']
            dept= las['DEPT']
            lit = las['LIT_T']
            kp = las['KP_T']
            kgt = las['KG_T']

            tmp_dept = []
            for i in range(len(dept)):
                if not math.isnan(kgt[i]):
                    tmp_dept.append(dept[i])
            if(len(tmp_dept) == 0):
                tmp_dept.append(0)
            ar_dept.append(tmp_dept[-1]-tmp_dept[0])

            for k in kp:
                if not (math.isnan(k)): 
                    k_por.append(k)
        
            for k in kgt:
            #    print(k)
                if not (math.isnan(k)):
                    k_nas.append(k)

        np.save("k_pors", k_por)
        np.save("k_nas", k_nas)
        np.save("heights", ar_dept)
        return (k_por, k_nas, ar_dept)
