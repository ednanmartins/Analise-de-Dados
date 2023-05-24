# Aula 33 - Teste prático Random Forest - Credit Data*
# Porem vou fazer com o Risco Credito

import pickle
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix
from sklearn.ensemble import RandomForestClassifier  # Biblioteca de Froresta Randomica


# Carregando os dados de treinamento e teste a partir do arquivo pickle
with open(
    "F:/Meus Documentos/Ednan Martins/Área de Trabalho/Ednan Pro/Cursos/Analise de Dados/01.Introd a Machine Learning com Python/Mod_04/risco_credito.pkl",
    "rb",
) as f:
    (x_risco_credito, y_risco_credito) = pickle.load(f)
x_risco_credito.shape, y_risco_credito.shape  # Teste visual

# Criando uma instância do classificador Random Forest
random_florest_risco_credito = RandomForestClassifier(
    n_estimators=10, criterion="entropy", random_state=0
)

# Treinando o modelo usando os dados de treinamento
random_florest_risco_credito.fit(x_risco_credito, y_risco_credito)

previsoes = random_florest_risco_credito.predict(x_risco_credito)
previsoes
y_risco_credito

accuracy_score(y_risco_credito, previsoes)

# Criando uma matriz de confusão usando o Yellowbrick
cm = ConfusionMatrix(random_florest_risco_credito)  # Cria instância
cm.fit(x_risco_credito, y_risco_credito)  # Ajusta a matriz
cm.score(x_risco_credito, y_risco_credito)  # Exibe a matriz e calcula pontuação
