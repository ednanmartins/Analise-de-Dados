# PROJETO PRÁTICO
"""Baixe o dataset disponível no Llink abaixo e faça o que se pede.
Link: https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification

Leia a descrição do dataset na página do Kaggle, lá você terá todas as informações sobre o mesmo e o que é necessário para realizar as previsões;
Realize os procedimentos de escalonamento, e tratamentos necessários;
Divida seus dados em treinamento e teste e salve em variáveis com o pickle;
Faça a previsão de falhas (ou não) na sua base de dados usando os três algoritmos estudados neste curso;
Veja a precisão dos três algoritmos usados neste curso com seus dados;
Redija um pequeno relatório analisando qual dos algoritmos foi mais eficiente em seus dados. Se possível, use gráficos para exemplificar melhor."""

import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv("predictive_maintenance.csv")
df.drop(columns="UDI", inplace=True)  # Exclui coluna UDI
df  # Teste visual
df.shape  # Teste de linhas e colunas

# PRIMEIRAS VERIFICAÇÕES:
# df.info()  # Verifica valores Nulos e Tipos de Dados
# df.describe()  # Mais algumas infos importantes


# ESSA PARTE AQUI NÃO SOU ESPECIALISTA :'(
x_df = df.iloc[:, 2:8].values
y_df = df.iloc[:, 8].values
x_df, y_df  # Teste visual

# Inicializando o objeto do escalonador
scaler_df = StandardScaler()

previsoes = scaler_df.fit_transform(x_df, y_df)
previsoes  # Teste visual

# Divisão dos dados de crédito em treinamento e teste
(
    x_df_treinamento,
    x_df_teste,
    y_df_treinamento,
    y_df_teste,
) = train_test_split(x_df, y_df, test_size=0.25, random_state=0)

# Salvando o conjunto de treinamento e teste do dataset  em formato pickle
with open("df.pkl", mode="wb") as f:
    pickle.dump([x_df_treinamento, y_df_treinamento, x_df_teste, y_df_teste], f)
