#%%

import pandas as pd 
import numpy as np


df = pd.read_csv("../data/clientes.csv", sep=";")

df.head()
# %%

df["pontosMais100"] = df["qtdePontos"] + 100

df.head()
# %%

df["EmailTwitch"] = df["flEmail"] + df["flTwitch"]
df.head()

#%%

df["flEmail"] + df["flTwitch"]

#%%

df["qtdePontos"].describe()

#%%

df["logPontos"] = np.log(df["qtdePontos"]+1)

df["logPontos"].describe

#%% 

import matplotlib.pyplot as plt

plt.hist(df["logPontos"])
plt.grid(True)
plt.show()   