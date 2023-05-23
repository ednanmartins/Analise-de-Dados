# Aula 14 - Divisão de Previsores e Classes

import pandas as pd

"""import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px  # Biblioteca de visualização de dados interativa"""

base_census = pd.read_csv("census.csv")

# Mostra somente as colunas
base_census.columns


# Selecionando as colunas de índice 0 a 13 do DF e obtendo os valores
x_census = base_census.iloc[:, 0:14].values
x_census  # Exibindo os valores de x_census

# Selecionando a coluna de índice 14 do DF e obtendo os valores
y_census = base_census.iloc[:, 14].values
y_census  # Exibindo os valores de y_census
