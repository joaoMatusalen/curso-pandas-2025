#Leia o arquivo transacoes.csv com a formatação correta;
#Adicione uma coluna com valores 1;
#Salve o dataframe com nome: transacoes_1.csv

#%%

import pandas as pd 

df = pd.read_csv("../../data/transacoes.csv", sep=";")
df['nova_coluna'] = 10
df.head(5)
df.to_csv('Transacoes_1.csv')