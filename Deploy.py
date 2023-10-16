#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import streamlit as st
import joblib
import numpy as np
pd.set_option('display.max_columns', 500)


# In[ ]:





# In[10]:


x_numericos = {'latitude': 0, 'longitude':0, 'accommodates':0, 'bathrooms':0, 'bedrooms':0, 'beds':0, 'security_deposit':0, 'extra_people':0, 'minimum_nights':0,'ano':0, 'mes':0, 'n_amenities':0, 'host_listings_count':0}

x_tf = {'host_is_superhost':0, 'instant_bookable':0}

x_listas = {'property_type':['Apartment', 'House', 'Condominium', 'Serviced apartment','Loft','Outros','Bed and breakfast','Hostel','Guest suite','Other','Guesthouse','Villa'],
            'room_type':['Entire home/apt', 'Private room', 'Shared room', 'Hotel room'],
            'cancellation_policy':['flexible', 'strict_14_with_grace_period', 'moderate', 'strict', 'super_strict_60', 'super_strict_30'],
            
}



dicionario = {}
for item in x_listas:
    for valor in x_listas[item]:
        dicionario[f'{item}_{valor}'] = 0


for item in x_numericos:
    if item == 'latitude' or item == 'longitude':
        valor = st.number_input(f'{item}', step=0.00001, value=0.0, format="%.5f")
    elif item == 'extra_people':
        valor = st.number_input(f'{item}', step=0.01, value=0.0)
    else:
        valor = st.number_input(f'{item}', step=1, value=0)
    x_numericos[item] = valor

for item in x_tf:
    valor = st.selectbox(f'{item}', ('Sim', 'Não'))
    if valor == "Sim":
        x_tf[item] = 1
    else:
        x_tf[item] = 0
    
    
for item in x_listas:
    valor = st.selectbox(f'{item}', x_listas[item])
    dicionario[f'{item}_{valor}'] = 1
    
botao = st.button('Prever Valor do Imóvel')

if botao:
    dicionario.update(x_numericos)
    dicionario.update(x_tf)
    valores_x = pd.DataFrame(dicionario, index=[0])
    
    dados = pd.read_csv('dadoss.csv')
    colunas = list(dados.columns)[1:-1]
    valores_x = valores_x[colunas]
    
    modelo = joblib.load('modelo.joblib')
    preco = modelo.predict(valores_x)
    st.write(preco[0])



# In[11]:


# x_numericos = {'latitude': 0, 'longitude':0, 'accommodates':0, 'bathrooms':0, 'bedrooms':0, 'beds':0, 'security_deposit':0, 'extra_people':0, 'minimum_nights':0,'ano':0, 'mes':0, 'n_amenities':0, 'host_listings_count':0}

# x_tf = {'host_is_superhost':0, 'instant_bookable':0}

# x_listas = {'property_type':['Apartment', 'House', 'Condominium', 'Serviced apartment','Loft','Outros','Bed and breakfast','Hostel','Guest suite','Other','Guesthouse','Villa'],
#             'room_type':['Entire home/apt', 'Private room', 'Shared room', 'Hotel room'],
#             'cancellation_policy':['flexible', 'strict_14_with_grace_period', 'moderate', 'strict', 'super_strict_60', 'super_strict_30'],
    
# }



# dicionario = {}
# for item in x_listas:
#     for valor in x_listas[item]:
#         dicionario[f'{item}_{valor}'] = 0


# for item in x_numericos:
#     if item == 'latitude' or item == 'longitude':
#         valor = st.number_input(f'{item}', step=0.00001, value=0.0, format="%.5f")
#     elif item == 'extra_people':
#         valor = st.number_input(f'{item}', step=0.01, value=0.0)
#     else:
#         valor = st.number_input(f'{item}', step=1, value=0)
#     x_numericos[item] = valor

# for item in x_tf:
#     valor = st.selectbox(f'{item}', ('Sim', 'Não'))
#     if valor == "Sim":
#         x_tf[item] = 1
#     else:
#         x_tf[item] = 0
    
    
# for item in x_listas:
#     valor = st.selectbox(f'{item}', x_listas[item])
#     dicionario[f'{item}_{valor}'] = 1
    
# botao = st.button('Prever Valor do Imóvel')

# if botao:
#     dicionario.update(x_numericos)
#     dicionario.update(x_tf)
#     valores_x = pd.DataFrame(dicionario, index=[0])
    
#     dados = pd.read_csv('dadoss.csv')
#     dados = dados.drop(columns=['is_business_travel_ready', 'bed_type_Outros', 'bed_type_Real Bed'])
#     colunas = list(dados.columns)[1:-1]
#     valores_x = valores_x[colunas]
    
#     modelo = joblib.load('modelo.joblib')
#     preco = modelo.predict(valores_x)
#     st.write(preco[0])



# In[ ]:




