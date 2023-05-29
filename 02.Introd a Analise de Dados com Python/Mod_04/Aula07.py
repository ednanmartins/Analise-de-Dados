# Aula 07 - Visualização de Dados com Gráfico Histograma

import numpy as np
import pandas as pd
import seaborn as sns
import yfinance as yf  # Biblioteca para acessar dados financeiros do Yahoo Finance
import matplotlib.pyplot as plt
from pandas_datareader import data

# import plotly.express as px

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

# sns.histplot(acoes_df["AMERICANAS"])

# Define o tamanho da figura do gráfico
plt.figure(figsize=(10, 50))

# Loop para plotar o histograma de cada coluna do DataFrame acoes_df
for i in np.arange(len(acoes_df.columns)):
    plt.subplot(7, 1, i + 1)  # Cria subplots para cada ação no DataFrame

    # Plota o histograma usando a função histplot() do seaborn
    sns.histplot(acoes_df[acoes_df.columns[i]])

    plt.title(acoes_df.columns[i])  # Define o título do gráfico como o nome da ação

    plt.tight_layout()  # Ajusta o layout dos subplots para evitar sobreposição de elementos

plt.show()  # Exibe o gráfico
