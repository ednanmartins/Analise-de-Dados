"""EXERCICIO PRÁTICO

1- Faça a leitura das bases de dados abaixo, e depois faça o que se pede em seguida:*

Bradesco, Banco do Brasil, Nubank, Itaú, Caixa Seguridade Participações e BOVA11

2- Sete o intervalo de 01/03/2019 até 31/12/2021.
3- Nomeie todas as colunas de modo a ficar simples a visualização.
4- Crie pelo menos um gráfico de cada um dos estudados, para as ações acima.
5- Normalize os dados das ações, e julgue a que achar mais rentável.
Por exemplo, ao final do seu intervalo de tempo, em qual você teria ganho mais dinheiro se investisse?

*Lembre-se de sempre buscar as ações brasileiras."""

import numpy as np
import pandas as pd
import seaborn as sns
import yfinance as yf  # Biblioteca para acessar dados financeiros do Yahoo Finance
import plotly.express as px
import matplotlib.pyplot as plt
from pandas_datareader import data

yf.pdr_override()

simb_bancos = [
    "BBDC3.SA",
    "BBAS3.SA",
    "NUBR33.SA",
    "ITUB3.SA",
    "CXSE3.SA",
    "BOVA11.SA",
]
start = "2019-03-01"
end = "2022-12-31"  # Mudei a data pois tinha muitos dados em branco

acoes_bancos = pd.DataFrame()

for banco in simb_bancos:
    acoes_bancos[banco] = data.get_data_yahoo(banco, start, end)["Close"]

acoes_bancos = acoes_bancos.rename(
    columns={
        "BBDC3.SA": "BRADESCO",
        "BBAS3.SA": "BB",
        "NUBR33.SA": "NUBANK",
        "ITUB3.SA": "ITAÚ",
        "CXSE3.SA": "CAIXA",
        "BOVA11.SA": "BOVA",
    }
)

acoes_bancos.isnull().sum()  # Soma dos valores nulos em cada coluna

acoes_bancos.to_csv("acoes_bancos.csv")
print("Salvo com Sucesso!!")

# GRAFICO DE HISTOGRAMA
for i in np.arange(len(acoes_bancos.columns)):
    plt.figure(figsize=(10, 50))  # plt.figure(figsize=(largura, altura))
    plt.subplot(7, 1, i + 1)
    sns.histplot(acoes_bancos[acoes_bancos.columns[i]])
    plt.title(acoes_bancos.columns[i])
    plt.tight_layout()
print(plt.show())

# GRAFICO DE BOXPLOT
for i in np.arange(len(acoes_bancos.columns)):
    plt.figure(figsize=(10, 50))  # plt.figure(figsize=(largura, altura))
    plt.subplot(7, 1, i + 1)
    sns.boxplot(acoes_bancos[acoes_bancos.columns[i]])
    plt.title(acoes_bancos.columns[i])
    plt.tight_layout()
    plt.show()

# GRAFICO DE LINHAS
acoes_bancos.plot(figsize=(15, 7), title="Histórico das Açõe dos Bancos")

# NORMALIZANDO DADOS
acoes_bancos_norm = acoes_bancos.copy()
for i in acoes_bancos_norm.columns[0:]:
    acoes_bancos_norm[i] = acoes_bancos_norm[i] / acoes_bancos_norm[i][0]

# GRAFICO DE LINHAS (NORMALIZADO)
acoes_bancos_norm.plot(
    figsize=(15, 7), title="Histórico das Ações dos Bancos (Normalizado)"
)

# GRAFICO DE LINHAS DINAMICO (NORMALIZADO)
figura = px.line(title="Histórico dos Preços das Ações dos Bancos (Normalizado)")
for i in acoes_bancos_norm.columns:
    figura.add_scatter(x=acoes_bancos_norm.index, y=acoes_bancos_norm[i], name=i)
figura.show()
