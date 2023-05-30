# Aula 19 - Implementação da Taxa de Retorno em Carteira de Ações

# import numpy as np
import pandas as pd

# import seaborn as sns
# import yfinance as yf  # Biblioteca para acessar dados financeiros do Yahoo Finance
# import plotly.express as px
# import matplotlib.pyplot as plt
# from pandas_datareader import data

dataset = pd.read_csv(
    "F:/Meus Documentos/Ednan Martins/Área de Trabalho/Ednan Pro/Cursos/Analise de Dados/02.Introd a Analise de Dados com Python/Mod_03/acoes.csv"
)
dataset_normalizado = dataset.copy()

# APLICANDO NORMALIZAÇÃO NO DATASET DUPLICADO
for i in dataset_normalizado.columns[1:]:
    dataset_normalizado[i] = dataset_normalizado[i] / dataset_normalizado[i][0]

# dataset_normalizado.plot(x="Date", figsize=(15, 7))  # Teste visuaç

# Deletando coluna Date
dataset_normalizado.drop(labels=["Date"], axis=1, inplace=True)

# TAXA DE RETORNO SIMPLES - Diário
retorno_carteira = (dataset_normalizado / dataset_normalizado.shift(1)) - 1
retorno_carteira  # Confirmação visual

# TAXA DE RETORNO SIMPLES - Anual (%)
retorno_anual = (retorno_carteira.mean() * 246) * 100
retorno_anual  # Confirmação visual
