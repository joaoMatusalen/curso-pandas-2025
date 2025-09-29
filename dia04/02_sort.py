#%% 

import pandas as pd 

df = pd.read_csv("../data/clientes.csv", sep=";")

df["qtdePontos"].sort_values()

#%%

df.sort_values(by="qtdePontos", ascending=False).head()

#%%

teste = pd.DataFrame(
    {

        "nome": ["Ana", "Carlos", "Maria", "João"],
        "idade": [23, 45, 18, 36],
        "salario": [2500, 5500, 2500, 4000]
    }
)

teste

#%%

teste.sort_values(by=["salario", "idade"], ascending=[False, True])        