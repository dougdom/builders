#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importa bibliotecas
import os
import pymongo
from pymongo import MongoClient
import dns
import json


# In[2]:


client = MongoClient("mongodb+srv://teste_dados_leitura:o7c4Cc8NDeXYbAMH@teste-dados.mcqmr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.teste_dados
collection = db.multas_2020


# In[3]:


collection.find()


# In[5]:


collection.replace("[]", "Sem informação")


# In[10]:


# carga dos dados do banco no arquivo json

with open('multas.json', 'a') as f:
    data = list()
    for item in collection.find():
        data.append(item)
    f.write(json.dumps(data, default=str))


# In[11]:


# substitui valores inválidos
with open('multas.json', 'r') as file:
     json_data = json.load(file)
     for item in json_data:
           if item['_id'] in ["60ab8f18ef5d383ce8403dfa","60ab8f18ef5d383ce8403e9b"]:
              item['amparo_legal'] = "Resolução ANTT Nº 233 DE 25/06/2003 Art. 1º, inciso I, alínea a "
              item['escopo_autuacao'] = "Transporte de passageiros"
           if item['mes'] in ["JANeIRO","JaNEIRO"]:
              item['mes'] = "JANEIRO"
           if item['uf'] in ["Es"]:
              item['uf'] = "ES"
           if item['uf'] in ["Mg"]:
              item['uf'] = "MG"
            
with open('multas.json', 'w') as file:
    json.dump(json_data, file, indent=2)


# In[ ]:




