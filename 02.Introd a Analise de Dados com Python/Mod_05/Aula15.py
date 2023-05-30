# Aula 15 - Verificando Taxa de Retorno Anual

import numpy as np
import pandas as pd

# import seaborn as sns
# import yfinance as yf  # Biblioteca para acessar dados financeiros do Yahoo Finance
# import plotly.express as px
import matplotlib.pyplot as plt

# from pandas_datareader import data

dataset = pd.read_csv(
    "F:/Meus Documentos/Ednan Martins/Área de Trabalho/Ednan Pro/Cursos/Analise de Dados/02.Introd a Analise de Dados com Python/Mod_03/acoes.csv"
)

# Calcula a taxa de retorno diária das Ações
dataset["RS AMERICANAS"] = (dataset["AMERICANAS"] / dataset["AMERICANAS"].shift(1)) - 1
dataset["RS CVC"] = (dataset["CVC"] / dataset["CVC"].shift(1)) - 1
dataset["RS WEGE"] = (dataset["WEGE"] / dataset["WEGE"].shift(1)) - 1
dataset["RS MAGALU"] = (dataset["MAGALU"] / dataset["MAGALU"].shift(1)) - 1
dataset["RS VIA"] = (dataset["VIA"] / dataset["VIA"].shift(1)) - 1
dataset["RS BOVA"] = (dataset["BOVA"] / dataset["BOVA"].shift(1)) - 1

lista = ["RS AMERICANAS", "RS CVC", "RS WEGE", "RS MAGALU", "RS VIA", "RS BOVA"]

# Loop para Printar Média de Retorno Simples e Plotar Grafico de Linhas
for i in np.arange(len(lista)):
    # Printa a Media Geral do Retorno Simples Anual de cada Ação
    print(f"Media Anual (%) da {lista[i]}: {((dataset[lista[i]].mean() * 246) * 100)}")

    plt.figure(figsize=(10, 20))  # Tamanho do contêiner (largura: 10, altura: 20)
    plt.subplot(6, 1, i + 1)  # Cria um subplot com 6 linhas, 1 coluna
    dataset[lista[i]].plot()  # Plota os valores da coluna atual (lista[i])
    plt.title(lista[i])  # Define o título do subplot
    plt.tight_layout()  # Ajusta o espaçamento entre os subplots
    plt.show()  # Exibe o gráfico do subplot atual
