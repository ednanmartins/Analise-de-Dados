# Aula 12 - Exploração de Dados

import pandas as pd

base_censo = pd.read_csv("census.csv")

# Importando o dataset e fazendo algumas consultas basicas
base_censo.head(5)
base_censo.describe
base_censo.isnull().sum()
