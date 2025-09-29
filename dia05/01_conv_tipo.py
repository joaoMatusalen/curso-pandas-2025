#%%

import pandas as pd 

df = pd.read_csv("../data/clientes.csv", sep=";")
df.head()

#%%

df["qtdePontos"].astype(float)

# %%

df["DtCriacao"] = pd.to_datetime(df["DtCriacao"])

#%%

df["DtCriacao"].replace({"2024-02-01 00:00:00.000" : "2025-02-01 00:00:00.000"})

# %%

df["DtCriacao"].dt.month_name()