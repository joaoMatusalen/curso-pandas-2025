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

#%%
uf["Área (km²)"] = uf["Área (km²)"].apply(str_to_float)
uf["População (Censo 2022)"] = uf["População (Censo 2022)"].apply(str_to_float)
uf["PIB (2015)"] = uf["PIB (2015)"].apply(str_to_float)
uf["PIB per capita (R$) (2015)"] = uf["PIB per capita (R$) (2015)"].apply(str_to_float)

#%%
uf.dtypes

#%%

def uf_to_regiao(uf):
    if uf in ["Distrito Federal", "Goiás", "Mato Grosso", "Mato Grosso do Sul"]:
        return "Centro-Oeste"
    elif uf in ["Alagoas","Bahia", "Ceará", "Maranhão", "Paraíba", "Pernambuco", "Piauí", "Rio Grande do Norte", "Sergipe"]:
        return "Nordeste"
    elif uf in ["Acre", "Amapá", "Amazonas", "Pará", "Rondônia", "Roraima", "Tocantins"]:
       return "Norte"
    elif uf in ["Espírito Santo","Minas Gerais", "Rio de Janeiro", "São Paulo"]:
        return "Sudeste"
    elif uf in ["Paraná", "Rio Grande do Sul", "Santa Catarina"]:
        return "Sul"
    
uf["Região"] = uf["Unidade federativa"].apply(uf_to_regiao)

uf

#%%

uf["PIB per capita (R$) (2015)"] > 30.000

#%%

def mortalidade_to_float(x):
    x = float(x.replace("‰", "")
               .replace(",", ".")
                )
    return x

uf["Mortalidade infantil (/1000)"] = uf["Mortalidade infantil (2016)"].apply(mortalidade_to_float)

#%%

def classifica_bom(linha):
    return (linha["PIB per capita (R$) (2015)"] > 30000 and
            linha["Mortalidade infantil (/1000)"] < 15 and 
            linha["IDH (2010)"] > 700)

#%%

uf["Classifica"] = uf.apply(classifica_bom, axis=1)


#%%

uf