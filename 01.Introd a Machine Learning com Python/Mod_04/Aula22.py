# Aula 22 - Teste Pratico Naïve Bayes - Risco Crédito

import pandas as pd
import pickle
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

# Leitura dos dados do arquivo CSV
base_risco_credito = pd.read_csv("risco_credito.csv")
base_risco_credito  # Teste visual

# Definição das colunas (GPT diz q é Col Entrada e Saida, mas discordo)
x_risco_credito = base_risco_credito.iloc[:, 0:4].values
y_risco_credito = base_risco_credito.iloc[:, 4].values
x_risco_credito  # Teste visual
y_risco_credito  # Teste visual

# Codificação das variáveis categóricas em x_risco_credito
label_encoder_historia = LabelEncoder()
label_encoder_divida = LabelEncoder()
label_encoder_garantias = LabelEncoder()
label_encoder_renda = LabelEncoder()

# Aplicação do LabelEncoder em cada coluna correspondente de x_risco_credito
x_risco_credito[:, 0] = label_encoder_historia.fit_transform(x_risco_credito[:, 0])
x_risco_credito[:, 1] = label_encoder_divida.fit_transform(x_risco_credito[:, 1])
x_risco_credito[:, 2] = label_encoder_garantias.fit_transform(x_risco_credito[:, 2])
x_risco_credito[:, 3] = label_encoder_renda.fit_transform(x_risco_credito[:, 3])
x_risco_credito  # Teste visual

# Salvando x_risco_credito e y_risco_credito em um arquivo pickle
with open("risco_credito.pkl", "wb") as f:
    pickle.dump([x_risco_credito, y_risco_credito], f)


# Criando uma instância do classificador Naïve Bayes
naive_risco_credito = GaussianNB()

# Treinando o modelo com os dados de entrada (x_risco_credito) e saída (y_risco_credito)
naive_risco_credito.fit(x_risco_credito, y_risco_credito)


""" ===========>> LEGENDA << ===========
[0, 0, 1, 2]            |   [2, 0, 0, 0]
historia boa (0)        |   historia ruim (2)
divida alta (0)         |   divida alta (0)
garantia nenhuma (1)    |   garantia adequada (0)
renda > 35 (2)          |   renda < 15 (0)"""
previsao = naive_risco_credito.predict([[0, 0, 1, 2], [2, 0, 0, 0]])
previsao  # Teste visual
naive_risco_credito.classes_  # Mostra as Classes Existentes
