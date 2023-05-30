# Aula 18 - Verificando Taxa de Retorno Logarítmica Diária e Anual

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
# print(dataset)

lista_normal = [
    "AMERICANAS",
    "CVC",
    "WEGE",
    "MAGALU",
    "VIA",
    "BOVA",
]
lista_logaritmica = [
    "RL AMERICANAS",
    "RL CVC",
    "RL WEGE",
    "RL MAGALU",
    "RL VIA",
    "RL BOVA",
]

# Um pequeno ajuste tecnico pra Americanas não ficar com linha quebrada
ult = len(dataset) - 1

# CALCULO DA TAXA DE RETORNO LOGARÍTMICA
rl_americanas = np.log(dataset["AMERICANAS"][ult] / dataset["AMERICANAS"][0]) * 100
rl_cvc = np.log(dataset["CVC"][len(dataset) - 1] / dataset["CVC"][0]) * 100
rl_wege = np.log(dataset["WEGE"][len(dataset) - 1] / dataset["WEGE"][0]) * 100
rl_magalu = np.log(dataset["MAGALU"][len(dataset) - 1] / dataset["MAGALU"][0]) * 100
rl_via = np.log(dataset["VIA"][len(dataset) - 1] / dataset["VIA"][0]) * 100
rl_bova = np.log(dataset["BOVA"][len(dataset) - 1] / dataset["BOVA"][0]) * 100

# LOOP COM CALCULO DE RETORNO LOGARITMO DIÁRIO
# A função 'zip' itera simultaneamente duas sequências
for lista_n, lista_l in zip(lista_normal, lista_logaritmica):
    dataset[lista_l] = np.log(dataset[lista_n] / dataset[lista_n].shift())

# Printa a Média Diária Geral Logaritmica das Ações
print(f"===>> Média Diária: <<===\n{dataset[lista_logaritmica].mean()}")

# Printa a Média Anual Geral Logaritmica das Ações
print(f"===> Média Anual (%): <===\n{((dataset[lista_logaritmica].mean()*246)*100)}")

dataset[lista_logaritmica[0]].plot(title=lista_logaritmica[0])

# Loop para Printar Média de Retorno Simples e Plotar Grafico de Linhas
for i in np.arange(len(lista_logaritmica)):
    # Printa a Media Geral do Retorno Simples Anual de cada Ação
    print(f"Média Diária: {(dataset[lista_logaritmica[i]].mean())*100}%")
    print(f"Média Anual: {((dataset[lista_logaritmica[i]].mean())*246)*100}%")

    plt.figure(figsize=(10, 20))  # Tamanho do contêiner (largura: 10, altura: 20)
    plt.subplot(6, 1, i + 1)  # Cria um subplot com 6 linhas, 1 coluna
    dataset[lista_logaritmica[i]].plot(title=lista_logaritmica[i])
    plt.tight_layout()  # Ajusta o espaçamento entre os subplots
    plt.show()  # Exibe o gráfico do subplot atual
