#%%
#05.01 - Crie uma coluna nova “twitch_points” que e resultado da multiplicação do saldo de pontos e a marcação da twitch

import pandas as pd

clientes = pd.read_csv("../../data/clientes.csv", sep=";")

clientes* ["Twitch_Points"] = clientes["qtdePontos"] * clientes["flTwitch"]

clientes.head()

#%%
#05.02 - Aplique o log na coluna de saldo de pontos, criando uma coluna nova

import numpy as np

clientes["pontosLog"] = np.log(clientes["qtdePontos"]+1)

clientes.head()

#%%
#05.03 - Crie uma coluna que sinalize se a pessoa tem vínculo com alguma (qualquer uma) plataforma de rede social.

clientes["vinculoSocialMedia"] = clientes["flEmail"] + clientes["flTwitch"] + clientes["flYouTube"] + clientes["flBlueSky"] + clientes["flInstagram"]

clientes.head()

#%%
#05.04 - Qual é o id de cliente que tem maior saldo de pontos? E o menor?

# Maior valor
clientes.sort_values(by=["qtdePontos", "idCliente"], ascending=[False, True]).head(1)

# Menor valor
clientes.sort_values(by=["qtdePontos", "idCliente"], ascending=[True, True]).head(1)

#%%
#05.05 - Selecione a primeira transação diária de cada cliente.

transacao = pd.read_csv("../../data/transacoes.csv", sep=";")

