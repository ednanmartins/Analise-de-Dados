# Aula 29 - Teste prático Árvore de decisão: Base de dados Census
""" ESSE CODIGO COMO O OUTRO, DEPENDE DO census.pkl QUE NÃO TRATOU
CORRETAMENTO O y_census, PORTANTO, ESTA COM O MESMO ERRO"""

import pickle
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier  # Biblioteca de Arvore de Decisão

# Carregando os dados de treinamento e teste a partir do arquivo pickle
with open(
    "F:/Meus Documentos/Ednan Martins/Área de Trabalho/Ednan Pro/Cursos/Analise de Dados/01.Introd a Machine Learning com Python/Mod_03/census.pkl",
    "rb",
) as f:
    (
        x_census_treinamento,
        y_census_treinamento,
        x_census_teste,
        y_census_teste,
    ) = pickle.load(f)
x_census_treinamento.shape, y_census_treinamento.shape  # Teste visual
x_census_teste.shape, y_census_teste.shape  # Teste visual

arvore_census = DecisionTreeClassifier(criterion="entropy", random_state=0)
arvore_census.fit(x_census_treinamento, y_census_treinamento)

previsoes = arvore_census.predict(x_census_teste)
previsoes
y_census_teste

accuracy_score(y_census_teste, previsoes)
