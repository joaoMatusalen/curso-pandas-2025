#%%

idades = [39, 30, 27, 18, 19, 20, 21, 22, 23, 24]

media = sum(idades) / len(idades)
media 

#%%

import pandas as pd 

series_idades = pd.Series(idades)
series_idades

#%%

series_idades.mean()
series_idades.var()


