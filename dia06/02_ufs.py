#%%

import pandas as pd
import requests

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

response = requests.get(url, headers=headers)
response.raise_for_status()  # levanta erro se a requisição falhar

dfs = pd.read_html(response.text)

uf = dfs[1]

#%%

def str_to_float(x):
    x = float(x.replace("", "")
              .replace(",", ".")
              .replace("\xa0", "")
              )
    return x

colunas = ["Área (km²)", "População (Censo 2022)", "PIB (2015)"]

uf[colunas].apply(str_to_float)