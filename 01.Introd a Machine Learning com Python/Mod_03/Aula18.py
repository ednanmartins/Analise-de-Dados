# Aula 18 - Divisão de Bases em Treinamento e Teste

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split


def trataIdade(dataset, col_idade):
    # Calcula a média dos valores não negativos
    media = dataset.loc[dataset[col_idade] >= 0, col_idade].mean()

    # Substitui os valores negativos pela média
    dataset.loc[dataset[col_idade] < 0, col_idade] = media
    # print("Idade negativa verificada e tratada!")

    # Preenche os valores ausentes com a média
    dataset[col_idade].fillna(media, inplace=True)
    # print("Idade null verificada e tratada!")


def refazX_credit():
    base_credit = pd.read_csv("credit_data.csv")

    if (base_credit["age"] < 0).any or (base_credit["age"].isnull()).any:
        trataIdade(base_credit, "age")

    x_credit = base_credit.iloc[:, 1:4].values

    return x_credit


def refazY_credit():
    base_credit = pd.read_csv("credit_data.csv")

    if (base_credit["age"] < 0).any or (base_credit["age"].isnull()).any:
        trataIdade(base_credit, "age")

    y_credit = base_credit.iloc[:, 4].values

    return y_credit


def refazX_census():
    base_census = pd.read_csv("census.csv")
    scaler_census = StandardScaler(with_mean=False)

    x_census = base_census.iloc[:, 0:14].values

    onehotencoder_census = ColumnTransformer(
        transformers=[("OneHot", OneHotEncoder(), [1, 3, 5, 6, 7, 8, 9, 13])],
        # remainder="passthrough" indica que as colunas não especificadas devem ser mantidas no resultado inalteradas.
        remainder="passthrough",
    )

    # Aplicando a codificação one-hot
    x_census = onehotencoder_census.fit_transform(x_census)

    # Aplicando o escalonamento
    x_census = scaler_census.fit_transform(x_census)

    return x_census


# Codigo construido com ajuda do ChatGPT
def refazY_census():
    base_census = pd.read_csv("census.csv")
    label_encoder = LabelEncoder()
    onehotencoder_y_census = OneHotEncoder()
    scaler_census = StandardScaler(with_mean=False)

    y_census = base_census.iloc[:, 14].values

    # Codificação numérica com LabelEncoder
    y_census = label_encoder.fit_transform(y_census)

    # Realiza a codificação one-hot na variável y_census
    # reshape(-1, 1) é usado para transformar o array unidimensional em uma matriz de coluna
    y_census = onehotencoder_y_census.fit_transform(y_census.reshape(-1, 1)).toarray()

    # Escalonamento com StandardScaler
    y_census = scaler_census.fit_transform(y_census)

    return y_census


# Codigo seguindo as aulas, mas o prof nao trata o y em nenhum momento
"""def refazY_census():
    base_census = pd.read_csv("census.csv")
    scaler_census = StandardScaler(with_mean=False)

    y_census = base_census.iloc[:, 14].values

    y_census = scaler_census.fit_transform(y_census)

    return y_census"""


x_credit = refazX_credit()
y_credit = refazY_credit()
x_census = refazX_census()
y_census = refazY_census()

# Divisão dos dados de crédito em treinamento e teste
(
    x_credit_treinamento,
    x_credit_teste,
    y_credit_treinamento,
    y_credit_teste,
) = train_test_split(x_credit, y_credit, test_size=0.25, random_state=0)

# Divisão dos dados de crédito em treinamento e teste
(
    x_census_treinamento,
    x_census_teste,
    y_census_treinamento,
    y_census_teste,
) = train_test_split(x_census, y_census, test_size=0.25, random_state=0)


print(x_credit_teste.shape, y_credit_teste.shape)
x_census_treinamento.shape, y_census_treinamento.shape
x_census_teste.shape, y_census_teste.shape
