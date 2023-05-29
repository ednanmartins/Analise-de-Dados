# Aula 11 - Visualização de Ações com Gráficos Dinâmicos

# import numpy as np
import pandas as pd

# import seaborn as sns
import yfinance as yf  # Biblioteca para acessar dados financeiros do Yahoo Finance
import plotly.express as px

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

acoes_df_nomalizado = acoes_df.copy()  # Duplica o DataFrame para preservar o original

for i in acoes_df_nomalizado.columns[0:]:  # Normalizando cada uma das Colunas
    acoes_df_nomalizado[i] = acoes_df_nomalizado[i] / acoes_df_nomalizado[i][0]

# Cria uma figura para o gráfico de linha
figura = px.line(title="Histórico dos Preços das Ações")

for i in acoes_df.columns[1:]:  # Adiciona um traçado para cada ação no gráfico de linha
    figura.add_scatter(x=acoes_df.index, y=acoes_df[i], name=i)

figura.show()  # Exibe o gráfico de linha

figura2 = px.line(title="Histórico dos Preços das Ações (Normalizado)")

for i in acoes_df_nomalizado.columns[1:]:
    figura2.add_scatter(x=acoes_df_nomalizado.index, y=acoes_df_nomalizado[i], name=i)

figura2.show()  # Exibe o gráfico de linha normalizado
