# Aula 19 - Salvando Variaveis

import pickle
from sklearn.model_selection import train_test_split
from Aula18 import refazX_census, refazX_credit, refazY_census, refazY_credit

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

# Salvando o conjunto de treinamento e teste do dataset  em formato pickle
with open("credit.pkl", mode="wb") as f:
    pickle.dump(
        [x_credit_treinamento, y_credit_treinamento, x_credit_teste, y_credit_teste], f
    )

with open("census.pkl", mode="wb") as f:
    pickle.dump(
        [x_census_treinamento, y_census_treinamento, x_census_teste, y_census_teste], f
    )
