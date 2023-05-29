# Aula 06 - Leitura de Base de Dados com Mais de uma Ação Financeira

import pandas as pd
import yfinance as yf  # Biblioteca para acessar dados financeiros do Yahoo Finance
from pandas_datareader import data

# Bibliotecas que serão utilizadas no modulo
"""import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt"""

# Ativa a função de substituição do pandas_datareader
yf.pdr_override()

simb_azul = "AZUL4.SA"
simb_acoes = ["AMER3.SA", "CVCB3.SA", "WEGE3.SA", "MGLU3.SA", "VIIA3.SA", "BOVA11.SA"]
start = "2015-01-01"

# Cria um DataFrame vazio para armazenar os dados das ações
acoes_df = pd.DataFrame()

# Loop para obter os dados históricos de cada ação
for acao in simb_acoes:
    # Obtém os dados históricos de fechamento da ação usando a função get_data_yahoo() do pandas_datareader
    # o '['Close']' no final, referencia que irá pegar apenas essa coluna
    acoes_df[acao] = data.get_data_yahoo(acao, start)["Close"]

# Renomeia as colunas do DataFrame para nomes mais amigáveis
acoes_df = acoes_df.rename(
    columns={
        "AMER3.SA": "AMERICANAS",
        "CVCB3.SA": "CVC",
        "WEGE3.SA": "WEGE",
        "MGLU3.SA": "MAGALU",
        "VIIA3.SA": "VIA",
        "BOVA11.SA": "BOVA",
    }
)

print(acoes_df)  # Imprime o DataFrame
print(acoes_df.isnull())  # Verifica se existem valores nulos
print(acoes_df.isnull().sum())  # Calcula a soma dos valores nulos em cada coluna
print(acoes_df.columns[0:])  # Imprime os nomes das colunas
print(acoes_df.describe())  # Imprime as estatísticas

# Salva os dados das ações em um arquivo CSV
acoes_df.to_csv("acoes.csv")

print("Dados salvo com sucesso!")  # Imprime uma mensagem de sucesso
