# Aula 32 - Teste prático Random Forest - Credit Data

import pickle
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix
from sklearn.ensemble import RandomForestClassifier  # Biblioteca de Froresta Randomica


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
x_credit_treinamento.shape, y_credit_treinamento.shape  # Teste visual
x_credit_teste.shape, y_credit_teste.shape  # Teste visual

# Criando uma instância do classificador Random Forest
random_florest_credit = RandomForestClassifier(
    n_estimators=100, criterion="entropy", random_state=0
)

# Treinando o modelo usando os dados de treinamento
random_florest_credit.fit(x_credit_treinamento, y_credit_treinamento)

previsoes = random_florest_credit.predict(x_credit_teste)
previsoes
y_credit_teste
accuracy_score(y_credit_teste, previsoes)

# Criando uma matriz de confusão usando o Yellowbrick
cm = ConfusionMatrix(random_florest_credit)  # Cria instância
cm.fit(x_credit_treinamento, y_credit_treinamento)  # Ajusta a matriz
cm.score(x_credit_teste, y_credit_teste)  # Exibe a matriz e calcula pontuação
