#%%

import pandas as pd

df = pd.DataFrame({

    "nome": ["Ana", "Bia", "Carlos", "Ana", "João", "Daniel", "Teo", "Bia", "Teo", "João"],
    "sobrenome": ["Silva", "Souza", "Silva", "Silva", "Pereira", "Matusalen", "Costa", "Matusalen", "Costa", "Pereira"],
    "salario": [1233, 2333, 4214, 3321, 2333, 5000, 6000, 2000, 6000, 5555]
})

df

#%%

df = (df.sort_values(by="salario", ascending=False)
        .drop_duplicates(keep="last", subset=["nome", "sobrenome"]))

df
#%%

