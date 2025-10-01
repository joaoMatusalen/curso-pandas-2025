#%%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")

transacoes.head()

#%%

transacoes.groupby(["IdCliente"]).count()

#%%

transacoes.groupby(["IdCliente"], as_index=False)[["IdTransacao"]].count()

#%%

transacoes.groupby(["IdCliente"], as_index=False).agg({"IdTransacao":['count'],
                                                       "QtdePontos": ['sum', 'mean']})

#%%

summary = transacoes.groupby(["IdCliente"], as_index=False).agg({"IdTransacao":['count'],
                                                       "QtdePontos": ['sum', 'mean']})

summary.head()

#%%

summary[("QtdePontos", "mean")]

#%%

summary.columns()