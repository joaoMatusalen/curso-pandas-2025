#%%

import pandas as pd

idades = [32, 18, 21, 22, 25, 63, 52, 63, 26, 74, 75, 112]
idades = pd.Series(idades)
idades

#%%

idades.sum()
idades.describe()

#%%

clientes = pd.read_csv("../data/clientes.csv", sep=";")

clientes
#%%

clientes["flTwitch"].sum()
clientes["flTwitch"].mean()

# %%

redes_sociais = ["flEmail",	"flTwitch",	"flYouTube",	"flBlueSky",	"flInstagram"]

clientes[redes_sociais].sum()
# %%

num_columns = clientes.dtypes[~(clientes.dtypes=="object")].index.tolist()

clientes[num_columns].mean()

#%%

clientes[num_columns].describe()