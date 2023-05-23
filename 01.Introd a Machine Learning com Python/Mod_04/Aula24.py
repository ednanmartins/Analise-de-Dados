# Aula 23 - Teste Pratico Naïve Bayes - Census
""" ESSE CODIGO EM ESPECIFICO NAO ESTA CORRETO, POIS NA AULA O PROF NAO TRATOU O
y_census, MAS NA CORREÇÃO DELE JA ESTAVA FEITO. ENTAO NAO VIMOS. MAS VOU TENTAR CORRIGIR"""

import pickle
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

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

# Correções necessario que o GPT provos, para rodar normalmente
x_census_treinamento = x_census_treinamento.toarray()
x_census_teste = x_census_teste.toarray()
y_census_treinamento = y_census_treinamento[:, 0]
y_census_treinamento = y_census_treinamento.astype(int)
y_census_teste = y_census_teste.astype(int)

x_census_treinamento.shape, y_census_treinamento.shape  # Teste visual

# Criando uma instância do classificador Naïve Bayes
naive_census = GaussianNB()

# Treinando o modelo usando os dados de treinamento
naive_census.fit(x_census_treinamento, y_census_treinamento)

# Fazendo previsões usando os dados de teste
previsoes = naive_census.predict(x_census_teste)
print("Previsoes: \n", previsoes)  # Teste visual
y_census_teste  # Saídas Reais para comparação manual

# Calcula acertividade das Previsões com as Saídas Reais
accuracy_score(y_census_teste, previsoes)

# Cria matriz de confusão para avaliar o desempenho do modelo
confusion_matrix(y_census_teste, previsoes)
