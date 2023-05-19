# Aula 07 - Tratamento de Dados Inconsistentes

import pandas as pd

"""import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px"""

# Importar arquivo CSV para o dataframe base_credit
base_credit = pd.read_csv("credit_data.csv")

# '.loc' faz uma consulta
base_credit.loc[base_credit["age"] < 0]
base_credit[base_credit["age"] < 0]  # Outro tipo de consulta

# Podemos usar a correção idiota de apagar a coluna inteira com:
base_credit2 = base_credit.drop("age", axis=1)
# 'axis=1' ou 'columns': refere-se ao eixo das colunas.
# 'axis=0' ou 'index': refere-se ao eixo das linhas
# 'axis' não pode ser definida dentro dos colchetes

# base_credit2


# Ou podemos pensar e retirar apenas as linhas, com:
base_credit3 = base_credit.drop(base_credit[base_credit["age"] < 0].index)

# base_credit3
# base_credit3[base_credit3["age"] < 0]  # Conferindo se deletou


# =====>> Agora vamos preencher essas linhas excluidas com a Media da idade do Dataset
# Para isso, usamos:
base_credit3.mean()  # Media de todos as colunas do Dataset
base_credit3["age"].mean()  # Media de coluna especifica

# =====>> Com a media encontrada e pulando todas aquelas contas desnecessarias do professor.
# Atribuimos essa media para as idades negativas:
base_credit.loc[base_credit["age"] < 0, "age"] = 40.92770044906

base_credit[base_credit["age"] < 0]  # Conferindo

base_credit.head(27)  # Conferindo visualmente
