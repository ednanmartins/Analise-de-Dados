# Aula 06 - Visualização de Dados

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# import plotly.express as px

# Importar arquivo CSV para o dataframe base_credit
base_credit = pd.read_csv("credit_data.csv")

# Utiliza a NumPy para obter valores únicos e contagem de ocorrências na coluna "default"
np.unique(base_credit["default"], return_counts=True)

# Cria gráfico de contagem dos valores da coluna "default"
# ';' Remove a legenda em cima do grafico, mas o formator não me deixa salvar
sns.countplot(x=base_credit["default"])

# Criar graficos de Historiograma com Matplot
plt.hist(x=base_credit["age"])
plt.hist(x=base_credit["income"])
plt.hist(x=base_credit["loan"])
