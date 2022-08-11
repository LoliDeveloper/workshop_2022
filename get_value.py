#!/usr/bin/env python
# coding: utf-8

# In[129]:


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
    print(gas_por)
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


# In[ ]:




