#%%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()

#%%
# Exemplo de filtro

joke = pd.DataFrame({
    "name": ["Chuck Norris", "Neil Armstrong", "Ed Sheeran"],
    "idade": [73, 12, 24],
    "uf": ["TX", "CA", "NY"]
})

filtro = joke["idade"] > 18

joke[filtro]

#%%

df = pd.read_csv("../data/transacoes.csv", sep=";")
df.head()

# Valores maiores ou iguais a 50 e menores que 100
filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)
df[filtro]

#%%

# Valores iguais a 1 ou 100
filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
df[filtro]

#%%

# Valores  maiores que 0 e menores ou iguais a 50 e data de criação maior que 2025-01-01
filtro = (df["QtdePontos"] > 0 ) & (df["QtdePontos"] <= 50) & (df["DtCriacao"] > "2025-01-01 ")
df[filtro]
