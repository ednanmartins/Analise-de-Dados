# Aula 28 - Teste prático Árvore de decisão: Base de dados Credit Data

import pickle
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier  # Biblioteca de Arvore de Decisão

# Carregando os dados de treinamento e teste a partir do arquivo pickle
with open(
    "F:/Meus Documentos/Ednan Martins/Área de Trabalho/Ednan Pro/Cursos/Analise de Dados/01.Introd a Machine Learning com Python/Mod_03/credit.pkl",
    "rb",
) as f:
    (
        x_credit_treinamento,
        y_credit_treinamento,
        x_credit_teste,
        y_credit_teste,
    ) = pickle.load(f)
x_credit_treinamento, y_credit_treinamento  # Teste visual
x_credit_teste, y_credit_teste  # Teste visual

# Criando uma instância de DecisionTreeClassifier com o critério de entropia
arvore_credit = DecisionTreeClassifier(criterion="entropy", random_state=0)

# Treinando o modelo com os dados de treinamento
arvore_credit.fit(x_credit_treinamento, y_credit_treinamento)

previsoes = arvore_credit.predict(x_credit_teste)
previsoes  # Teste visual
y_credit_teste  # Teste de comparação visual
accuracy_score(y_credit_teste, previsoes)  # Acertibilidade das Previsoes
