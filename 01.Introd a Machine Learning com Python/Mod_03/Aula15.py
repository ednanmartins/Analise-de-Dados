# Aula 15 - Tratamento de Atributos Categoricos: Label Encoder

import pandas as pd
from sklearn.preprocessing import (
    LabelEncoder,
)  # Codificar rótulos categóricos em valores numéricos.

"""import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px  # Biblioteca de visualização de dados interativa"""

base_census = pd.read_csv("census.csv")

# Inicializando objetos LabelEncoder para cada atributo categórico a ser codificado
label_encoder_workclass = LabelEncoder()
label_encoder_education = LabelEncoder()
label_encoder_marital = LabelEncoder()
label_encoder_occupation = LabelEncoder()
label_encoder_relationship = LabelEncoder()
label_encoder_race = LabelEncoder()
label_encoder_sex = LabelEncoder()
label_encoder_country = LabelEncoder()

# Obtendo os valores dos atributos previsores (x_census) e da classe alvo (y_census)
x_census = base_census.iloc[:, 0:14].values
y_census = base_census.iloc[:, 14].values

print(x_census[0])  # Antes da tranformação
# Ajusta e transforma os dados da coluna 1 de x_census usando o label_encoder_teste
# fit_transform() é uma combinação das etapas de ajuste (fitting) e transformação (transform) aplicadas a um estimador em um único passo.

# Aplicando o LabelEncoder a cada coluna categórica de x_census
x_census[:, 1] = label_encoder_workclass.fit_transform(x_census[:, 1])
x_census[:, 3] = label_encoder_education.fit_transform(x_census[:, 3])
x_census[:, 5] = label_encoder_marital.fit_transform(x_census[:, 5])
x_census[:, 6] = label_encoder_occupation.fit_transform(x_census[:, 6])
x_census[:, 7] = label_encoder_relationship.fit_transform(x_census[:, 7])
x_census[:, 8] = label_encoder_race.fit_transform(x_census[:, 8])
x_census[:, 9] = label_encoder_sex.fit_transform(x_census[:, 9])
x_census[:, 13] = label_encoder_country.fit_transform(x_census[:, 13])

x_census[0]  # Depois da tranformação
