# Aula 13 - Visualização de Dados

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px  # Biblioteca de visualização de dados interativa

base_censo = pd.read_csv("census.csv")

# Consulta basica com Numpy pra ver quantos tem renda <= ou > que 50k
np.unique(base_censo["income"], return_counts=True)

# Grafico de Barras com Seabornque exibe a mesma informação acima
sns.countplot(x=base_censo["income"])

# Grafico de Histotiograma com Matplot para exibir Idade
plt.hist(x=base_censo["age"])
plt.hist(x=base_censo["hour-per-week"])

# Grafico dinamico com Plotly
# 'treemap' é um Mapa de Arvore
# Cria um gráfico treemap com base nos dados de 'base_censo',
# utilizando as colunas 'workclass' e 'age' para definir a hierarquia
grafico = px.treemap(base_censo, path=["workclass", "age"])

# Gráfico de treemap com 'base_censo', utilizando as colunas 'occupation', 'relationship' e 'age'
grafico = px.treemap(base_censo, path=["occupation", "relationship", "age"])

# Gráfico de categorias paralelas com 'base_censo', utilizando as dimensões 'occupation' e 'relationship'
grafico = px.parallel_categories(base_censo, dimensions=["occupation", "relationship"])
grafico.show()  # Exibe o gráfico treemap
