#%% 

import pandas as pd


#06.01 - Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?
#06.02 - Quais são os usuários que mais fizeram transações? Considere os 10 primeiros.
#06.03 - Qual usuário teve maior quantidade de pontos debitados?
#%%
#06.04 - Quem teve mais transações de Streak?

transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")

transacao_produto = pd.read_csv("../../data/transacao_produto.csv", sep=";")

produtos = pd.read_csv("../../data/produtos.csv", sep=";")

produtos["IdProduto"] = produtos["IdProduto"].astype(str)

#%%
df = (transacoes.merge(right=transacao_produto, how="left", on="IdTransacao")
                .merge(right=produtos, how="left", on="IdProduto"))

filtro = df["IdProduto"] == "12"

df_full = (df[filtro].groupby(["IdCliente"], as_index=False)
                     .agg({"IdTransacao" : "count"})
                     .sort_values("IdTransacao", ascending=False)
                     .head(3)
                    )
        
df_full.columns = ["IdCliente", "QtdeStreak"]

df_full
#%%
#06.05 - Qual a média de transações / dia?
#06.06 - Como podemos calcular as estatísticas descritivas dos pontos das transações de cada usuário?
