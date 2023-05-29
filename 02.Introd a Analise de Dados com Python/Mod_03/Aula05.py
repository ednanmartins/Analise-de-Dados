# Aula 05 - Analise de Dados e Estatistica Básica

import yfinance as yf  # Biblioteca para acessar dados financeiros do Yahoo Finance
from pandas_datareader import data

# Bibliotecas que serão utilizadas no modulo
"""import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt"""

# Ativa a função de substituição do pandas_datareader
yf.pdr_override()

simbolo = "AZUL4.SA"
start = "2017-01-01"

# Obtém os dados do Yahoo Finance usando a função get_data_yahoo
azul_df = data.get_data_yahoo(simbolo, start)
# print(azul_df.info())  # Imprime informação do DF
# print(azul_df.head(3))  # Imprime as 3 primeiras linhas
# print(azul_df.tail(3))  # Imprime as 3 ultimas linhas
# print(azul_df.describe())  # Imprime dados estatisticos
# print(azul_df[azul_df["Close"] >= 39.21])  # Imprime de acordo com condição passada
# print(azul_df[azul_df["Close"] == 10.35])  # Imprime de acordo com condição passada
# print(azul_df[(azul_df["Close"] >= 10.34) & (azul_df["Close"] <= 10.36)])  # 2 condições

azul_df.to_csv("azul.csv")  # Salvar o arquivo na pasta
print("Salvo com sucesso!!")
