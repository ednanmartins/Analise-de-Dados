# Aula 08 - Tratamento de Dados Faltantes

import pandas as pd

"""import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px"""


def substituiIdadeNegativaPelaMedia(dataset, col_idade):
    new_dataset = dataset.drop(dataset[dataset[col_idade] < 0].index)
    media = new_dataset[col_idade].mean()
    dataset.loc[dataset[col_idade] < 0, col_idade] = media
    return dataset


base_credit = pd.read_csv("credit_data.csv")

# '.any()' é utilizado pra verificar se pelo menos um elemento é verdadeiro.
# Neste caso verifica se existe 'base_credit['age]' é menor que 0
if (base_credit["age"] < 0).any:
    # Se sim, ele entra na função, onde passo as variaveis necessarias
    substituiIdadeNegativaPelaMedia(base_credit, "age")
else:
    print("Vish, passou!")

# Verifica se tem dados em branco
base_credit.isnull()  # Vai mostrar linha por linha
base_credit.isnull().sum()  # Vai somar a quantidade em cada coluna
# Localiza na coluna "age" onde tem valores nulos.
base_credit.loc[pd.isnull(base_credit["age"])]

# '.fillna()' É um método que preenche os valores ausentes (nulos). No caso (base_credit["age"].mean() = Media)
""" inplace=True: É um parâmetro opcional do método fillna(). # Quando definido
como True, indica que as alterações devem ser feitas diretamente no DataFrame
base_credit, em vez de retornar um novo DataFrame com os valores preenchidos."""
base_credit["age"].fillna(base_credit["age"].mean(), inplace=True)


# Aquela velha conferida basica
base_credit.loc[pd.isnull(base_credit["age"])]

# Verificar visualmente de acordo com o id
# '.isin()' Verifica se cada valor da coluna está presente na lista
base_credit.loc[base_credit["clientid"].isin([16, 22, 27, 29, 31, 32])]
