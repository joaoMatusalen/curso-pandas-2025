#%%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=";")
df

#%%

df.to_csv("../dia02/clientes.csv")
# %%

df.to_parquet("../dia02/clientes.parquet", index=False)

#%%

df_2 = pd.read_parquet("../dia02/clientes.parquet")
df_2

#%%

df.to_excel("../dia02/clientes.xlsx", index=False)

#%%

df_3 = pd.read_excel("../dia02/clientes.xlsx")
df_3    

#%%