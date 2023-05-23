# Aula 23 - Teste Pratico Naïve Bayes - Credit Data

import pickle
from sklearn.naive_bayes import GaussianNB
from yellowbrick.classifier import ConfusionMatrix
from sklearn.metrics import accuracy_score, confusion_matrix

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

# Exibindo as dimensões dos dados de treinamento e teste
x_credit_treinamento.shape, y_credit_treinamento.shape
x_credit_teste.shape, y_credit_teste.shape

# Criando uma instância do classificador Naïve Bayes
naive_credit_data = GaussianNB()

# Treinando o modelo usando os dados de treinamento
naive_credit_data.fit(x_credit_treinamento, y_credit_treinamento)

# Fazendo previsões usando os dados de teste
previsoes = naive_credit_data.predict(x_credit_teste)
previsoes  # Teste visual
y_credit_teste  # Saídas Reais para comparação manual

# Calcula acertividade das Previsões com as Saídas Reais
accuracy_score(y_credit_teste, previsoes)

# Cria matriz de confusão para avaliar o desempenho do modelo
confusion_matrix(y_credit_teste, previsoes)

# Criando Modelo Visual da Matriz de Confusão com o Yellowbrick
cm = ConfusionMatrix(naive_credit_data)  # Cria instância
cm.fit(x_credit_treinamento, y_credit_treinamento)  # Ajusta Matriz
cm.score(x_credit_teste, y_credit_teste)  # Calcula pontuação do Modelo
