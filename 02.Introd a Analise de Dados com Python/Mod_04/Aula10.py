# Aula 10 - Normalização de Dados para Análise Real

# import numpy as np
import pandas as pd

# import seaborn as sns
import yfinance as yf  # Biblioteca para acessar dados financeiros do Yahoo Finance

# import plotly.express as px
# import matplotlib.pyplot as plt
from pandas_datareader import data

yf.pdr_override()  # Ativa a função de substituição do pandas_datareader

simb_azul = "AZUL4.SA"
simb_acoes = ["AMER3.SA", "CVCB3.SA", "WEGE3.SA", "MGLU3.SA", "VIIA3.SA", "BOVA11.SA"]
start = "2015-01-01"

acoes_df = pd.DataFrame()  # Cria um DataFrame vazio

for acao in simb_acoes:  # Loop para obter os dados de cada Ação
    # Obtém os dados históricos de fechamento da ação usando a função get_data_yahoo() do pandas_datareader
    # o '['Close']' no final, referencia que irá pegar apenas essa coluna
    acoes_df[acao] = data.get_data_yahoo(acao, start)["Close"]

acoes_df = acoes_df.rename(  # Renomeia as colunas
    columns={
        "AMER3.SA": "AMERICANAS",
        "CVCB3.SA": "CVC",
        "WEGE3.SA": "WEGE",
        "MGLU3.SA": "MAGALU",
        "VIIA3.SA": "VIA",
        "BOVA11.SA": "BOVA",
    }
)

# print(acoes_df)  # Printa dados em texto
# acoes_df.plot(figsize=(15, 7), title="Histórico das Ações")  # Plota Gráfico de Linhas

acoes_df_nomalizado = acoes_df.copy()  # Duplica o DataFrame

for i in acoes_df_nomalizado.columns[0:]:  # Normalizando cada uma das Colunas
    acoes_df_nomalizado[i] = acoes_df_nomalizado[i] / acoes_df_nomalizado[i][0]

# print(acoes_df_nomalizado)
acoes_df_nomalizado.plot(figsize=(15, 7), title="Histórico das Ações (Normalizado)")
