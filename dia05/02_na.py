#%% 

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes

# %%
clientes = clientes.dropna(how="any")

# %%

df = pd.DataFrame (
    {
        "nome": ["Ana", "Bia", None],
        "idade": [20, None, 30],
        "salario": [2000, 3000, None]
    }
)

df.dropna(how="all", subset=["salario"])
# %%

df["idade"] = df["idade"].fillna(0)
df

#%%

