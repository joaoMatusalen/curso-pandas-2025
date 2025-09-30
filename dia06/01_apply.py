#%%

import pandas as pd 

df = pd.read_csv("../data/clientes.csv", sep=";")

df.head()

#%%

def get_last_id(x):
    return x.split("-")[-1]

#%%
df["idNovo"] = df["idCliente"].apply(get_last_id)

df.head()