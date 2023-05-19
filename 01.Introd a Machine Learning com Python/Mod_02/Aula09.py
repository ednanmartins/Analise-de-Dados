# Aula 09 - Divisão entre previsores e classes

import pandas as pd

"""import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px"""


# Função 1 milhão de vezes superior ao exercico, pois não cria um novo dataset e trata os 2 problemas com uma unica função
# Estao função não precisa de um return, pois trata o proprio dataset passado como argumento
def trataIdade(dataset, col_idade):
    # Calcula a média dos valores não negativos
    media = dataset.loc[dataset[col_idade] >= 0, col_idade].mean()

    # Substitui os valores negativos pela média
    dataset.loc[dataset[col_idade] < 0, col_idade] = media
    # print("Idade negativa verificada e tratada!")

    # Preenche os valores ausentes com a média
    dataset[col_idade].fillna(media, inplace=True)
    # print("Idade null verificada e tratada!")


def substituiIdadeNegativaPelaMedia(dataset, col_idade):
    new_dataset = dataset.drop(dataset[dataset[col_idade] < 0].index)
    media = new_dataset[col_idade].mean()
    dataset.loc[dataset[col_idade] < 0, col_idade] = media
    return dataset


def preencheIdadeEmBranco(dataset, col_idade):
    dataset[col_idade].fillna(dataset[col_idade].mean(), inplace=True)


base_credit = pd.read_csv("credit_data.csv")

if (base_credit["age"] < 0).any or (base_credit["age"].isnull()).any:
    trataIdade(base_credit, "age")
    print("Idade tratada com Sucesso!")
else:
    print("Vish, passou!")

# Printa as colunas que EU SABIA que estava errado, para conferir se corrigiu
# print(base_credit.loc[base_credit["clientid"].isin([16, 22, 27, 29, 31, 32])])


#  'iloc' é usado para indexar e selecionar dados em um DataFrame ou Series
# Sintaxe geral: dataframe.iloc[linhas, colunas]
"""dataframe.iloc[0]  # Seleciona a primeira linha do DataFrame
dataframe.iloc[:, 0]  # Seleciona a primeira coluna do DataFrame
dataframe.iloc[1:5, 2:4]  # Seleciona um intervalo de linhas e colunas do DataFrame"""


# Seleciona as colunas de índice 1 a 3 como previsores e obtém seus valores
x_credit = base_credit.iloc[:, 1:4].values
print(x_credit)

# Seleciona a coluna de índice 4 como classe ou alvo e obtém seus valores
y_credit = base_credit.iloc[:, 4].values
y_credit


# CURIOSIDADE
type(base_credit)  # pandas.core.frame.DataFrame
type(x_credit)  # numpy.ndarray
type(y_credit)  # numpy.ndarray
