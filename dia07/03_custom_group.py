#%% 

import pandas as pd 
import numpy as np

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")

transacoes.head()
#%%

def diff_amp(x):
    amplitude = x.max() - x.min()
    media = x.mean()
    return np.sqrt((amplitude - media)**2)

def life_time(x):
    dt = pd.to_datetime(x)
    return (dt.max() - dt.min()).days

#%%

summary = (transacoes.groupby(["IdCliente"], as_index = False)
           .agg({
               "IdTransacao": ['count'],
               "QtdePontos": ['sum', 'mean', diff_amp],
               "DtCriacao": [life_time]
           }))

summary.columns =[
    "IdCliente",
    "QtdeIdTransacao",
    "QtdePontosSum",
    "QtdePontosMean",
    "QtdePontosAmp",
    "LifeTime"
]

summary