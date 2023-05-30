# Aula 22 - Comparando Fundo de Ações com a Bovespa

# import numpy as np
import pandas as pd

# import seaborn as sns
# import yfinance as yf  # Biblioteca para acessar dados financeiros do Yahoo Finance
import plotly.express as px

# import matplotlib.pyplot as plt
# from pandas_datareader import data

dataset = pd.read_csv(
    "F:/Meus Documentos/Ednan Martins/Área de Trabalho/Ednan Pro/Cursos/Analise de Dados/02.Introd a Analise de Dados com Python/Mod_03/acoes.csv"
)
dataset_normalizado = dataset.copy()

# APLICANDO NORMALIZAÇÃO NO DATASET DUPLICADO
for i in dataset_normalizado.columns[1:]:
    dataset_normalizado[i] = dataset_normalizado[i] / dataset_normalizado[i][0]

# Calcula a média dos valores normalizados das ações selecionadas para compor a carteira
dataset_normalizado["CARTEIRA"] = (
    dataset_normalizado["AMERICANAS"]
    + dataset_normalizado["CVC"]
    + dataset_normalizado["WEGE"]
    + dataset_normalizado["MAGALU"]
    + dataset_normalizado["VIA"]
) / 5
# dataset_normalizado.head(5)  # Confirmação visual


# Cria o gráfico comparativo entre a carteira e o índice BOVA
figura = px.line(title="Comparativo Carteira x BOVA")

# Adiciona as linhas no gráfico para cada coluna do dataset normalizado
for i in dataset_normalizado.columns[1:]:
    figura.add_scatter(x=dataset_normalizado["Date"], y=dataset_normalizado[i], name=i)
figura.show()  # Exibe o gráfico


# Remove as colunas das ações individuais, mantendo apenas a coluna da carteira
dataset_normalizado.drop(
    ["AMERICANAS", "CVC", "WEGE", "MAGALU", "VIA"], axis=1, inplace=True
)


# Cria outro gráfico comparativo apenas com a carteira e o índice BOVA
figura = px.line(title="Comparativo Carteira x BOVA")

# Adiciona as linhas no gráfico para cada coluna do dataset normalizado (agora apenas com a carteira)
for i in dataset_normalizado.columns[1:]:
    figura.add_scatter(x=dataset_normalizado["Date"], y=dataset_normalizado[i], name=i)
figura.show()  # Exibe o segundo gráfico
