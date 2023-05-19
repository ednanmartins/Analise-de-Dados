# Aula 04 - Exploração de Dados

import pandas as pd

# Importar arquivo CSV para o dataframe base_credit
base_credit = pd.read_csv("credit_data.csv")

base_credit  # Chamando o banco inteiro
base_credit.head(10)  # Os 10 primeiros
base_credit.tail(10)  # Os 10 ultimos
base_credit.describe()  # Dados estatisticos
base_credit[base_credit["income"] >= 69995]  # Exibe de acordo com a condição passada
