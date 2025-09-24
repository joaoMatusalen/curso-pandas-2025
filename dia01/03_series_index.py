#%%
import pandas as pd

idades = [39, 30, 27, 18, 19, 20, 21, 22, 23, 24]

series_idades = pd.Series(idades)
series_idades

#%%

series_idades[0]

#%%
series_idades = series_idades.sort_values() 

#series_idades[0]

#%%

series_idades.iloc[0]

#%%

series_idades.iloc[:3]

#%%

idades = [39, 30, 27, 18, 19, 20, 21, 22, 23, 24]

indexs = ['João', 'Maria', 'Pedro', 'Ana', 'José', 'Paula', 'Lucas', 'Laura', 'Marcos', 'Julia']

series_idades = pd.Series(idades, index=indexs)
series_idades

#%%

series_idades['João']

#%%

series_idades.iloc[2]