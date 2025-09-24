#%%
import pandas as pd

idades = [39, 30, 27, 18, 19, 20, 21, 22, 23, 24]

nomes = ['João', 'Maria', 'Pedro', 'Ana', 'José', 'Paula', 'Lucas', 'Laura', 'Marcos', 'Julia']

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

#%%

df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes
df

#%%
df["nomes"]

#%%

df.iloc[0]

#%%

