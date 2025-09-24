#%%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")

df
#%%

df.shape

#%%

df.info(memory_usage='deep')

#%%

df.dtypes

#%%

df.rename(columns={"QtdePontos": "QtdPontos",
                        "DescSistemaOrigem": "SistemaOrigem"}, inplace=True)

#%%

df.dtypes

#%%

df["IdCliente"]

#%%

df[["IdCliente", "QtdPontos"]]

#%%

df[["IdCliente", "QtdPontos", "IdTransacao"]].head(5)

#%%

colunas = list(df.columns)
colunas.sort()
df[colunas]