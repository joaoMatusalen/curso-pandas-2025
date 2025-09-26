#%%
#04.01 - Quantos clientes tem vínculo com a Twitch?

import pandas as pd

clientes = pd.read_csv("../../data/clientes.csv", sep=";")
clientes

filtro = clientes["flTwitch"] == 1

qtdViculosTwitch = clientes[filtro].shape[0]

print(f"Existem {qtdViculosTwitch} clientes com vínculo com a Twitch!")

#%%
#04.02 - Quantos clientes tem um saldo de pontos maior que 1000?

filtro = clientes["qtdePontos"] > 1000

qtdMaior1000Pontos = clientes[filtro].shape[0]

print(f"Existe {qtdMaior1000Pontos} clientes com um saldo maior que 1000!")

#%%
#04.03 - Quantas transações ocorreram no dia 2025-02-01?

import pandas as pd

transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")

transacoes.head()

filtro = (transacoes['DtCriacao'] >= '2025-02-01') & (transacoes['DtCriacao'] < '2025-02-02')

transacoes[filtro]
