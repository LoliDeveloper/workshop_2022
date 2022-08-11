#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_value(k_gas,k_por,h,S,mat,P):
    temp_value=[]
    value = []
    for i in range(len(k_gas)):
        temp_value.append(k_gas[i]*k_por[i]*h[i]/2)
    for i in range(len(k_gas)):
        for V in range(len(mat[i])):
            if V > 0:
                temp_value[i] += mat[i][V] / P[i] * temp_value[V]
        temp_value[i] = [S[i] * x for x in temp_value]
    return temp_value


# In[ ]:


def get_value2(k_gas,k_por,h,S,mat,P):
    '''Считаем произведение вероятностей. Каждое значение перемножается с каждым другим. Перемножаем k_por k_gas h'''
    gas_por = []
    for i in range (k_gas):
        for gas in k_gas[i]:
            for por in k_por[i]:
                temp.append(gas*por)
        temp = [x*h[i] for x in temp]
        
        gas_por.append(temp)
   
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
        adskoe_raspredelenie.append(save)                


# In[ ]:




