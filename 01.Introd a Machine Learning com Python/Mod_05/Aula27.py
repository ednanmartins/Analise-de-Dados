# Aula 27 - Teste prático Árvore de decisão: Base de dados Risco de Crédito

import pickle
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier  # Biblioteca de Arvore de Decisão

# Carregando os dados de treinamento e teste a partir do arquivo pickle
with open(
    "F:/Meus Documentos/Ednan Martins/Área de Trabalho/Ednan Pro/Cursos/Analise de Dados/01.Introd a Machine Learning com Python/Mod_04/risco_credito.pkl",
    "rb",
) as f:
    x_risco_credito, y_risco_credito = pickle.load(f)
x_risco_credito, y_risco_credito  # Teste visual

# Criando uma instância de DecisionTreeClassifier com o critério de entropia
arvore_risco_credito = DecisionTreeClassifier(criterion="entropy")

# Treinando o modelo com os dados de treinamento
arvore_risco_credito.fit(x_risco_credito, y_risco_credito)

# Obtendo a importância das features (variáveis) na árvore de decisão
arvore_risco_credito.feature_importances_

# Obtendo as classes (rótulos) da árvore de decisão
arvore_risco_credito.classes_

# Definindo os nomes das features (variáveis) para exibição da árvore de decisão
previsores = ["historia", "dívida", "garantias", "renda"]

# Criando uma figura e eixos para exibir a árvore de decisão
figura, eixos = plt.subplots(nrows=1, ncols=1, figsize=(10, 10))

# Exibindo a árvore de decisão
tree.plot_tree(
    arvore_risco_credito,
    feature_names=previsores,
    class_names=arvore_risco_credito.classes_,
    filled=True,
)

# Realizando previsões com a árvore de decisão
previsoes = arvore_risco_credito.predict([[0, 0, 1, 2], [2, 0, 0, 0]])
previsoes  # Teste visual
