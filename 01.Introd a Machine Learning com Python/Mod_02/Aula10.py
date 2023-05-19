# Aula 10 - Escalonamento de Valores

import pandas as pd
from sklearn.preprocessing import StandardScaler  # Usada para padronização de dados

"""import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px"""


# Função 1 milhão de vezes superior ao exercico
def trataIdade(dataset, col_idade):
    # Calcula a média dos valores não negativos
    media = dataset.loc[dataset[col_idade] >= 0, col_idade].mean()

    # Substitui os valores negativos pela média
    dataset.loc[dataset[col_idade] < 0, col_idade] = media
    # print("Idade negativa verificada e tratada!")

    # Preenche os valores ausentes com a média
    dataset[col_idade].fillna(media, inplace=True)
    # print("Idade null verificada e tratada!")


base_credit = pd.read_csv("credit_data.csv")

if (base_credit["age"] < 0).any or (base_credit["age"].isnull()).any:
    trataIdade(base_credit, "age")
    # print("Idade tratada com Sucesso!")
else:
    print("Vish, passou!")

# Seleciona as colunas de índice 1 a 3 como previsores e obtém seus valores
x_credit = base_credit.iloc[:, 1:4].values
x_credit

# Seleciona a coluna de índice 4 como classe ou alvo e obtém seus valores
y_credit = base_credit.iloc[:, 4].values
y_credit

# Obtém o valor mínimo e maximo de cada coluna
x_credit[:, 0].min(), x_credit[:, 1].min(), x_credit[:, 2].min()
x_credit[:, 0].max(), x_credit[:, 1].max(), x_credit[:, 2].max()


"""Cria uma instância da classe StandardScaler, usada para
realizar o pré-processamento de padronização dos dados"""
scaler_credit = StandardScaler()

# Aplica o pré-processamento de padronização aos dados em x_credit
# O método fit_transform realiza dois passos: ajusta (fit) os parâmetros do scaler aos dados e em seguida transforma (transform) os dados
x_credit = scaler_credit.fit_transform(x_credit)

print(x_credit[:, 0].min(), x_credit[:, 1].min(), x_credit[:, 2].min())
x_credit[:, 0].max(), x_credit[:, 1].max(), x_credit[:, 2].max()
