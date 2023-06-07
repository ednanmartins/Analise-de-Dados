"""EXERCICIO PRÁTICO


Usando a base de dados gerada no EXERÍCIO PRÁTICO da aula 14,calcule as taxas de retorno desta
carteira de ações e calcule o risco desta carteira, bem como gere a matriz de correlação.

Compare o resultado desta carteira com a BOVA e responda à pergunta abaixo:

Qual das ações, sua carteira ou a BOVA possui maior risco de investimento?

Justifique!"""

import math
import numpy as np
import pandas as pd

base_acoes = pd.read_csv(
    "F:/Meus Documentos/Ednan Martins/Área de Trabalho/Ednan Pro/Cursos/Analise de Dados/02.Introd a Analise de Dados com Python/Mod_03/acoes.csv"
)
base_acoes.drop(labels=["Date"], axis=1, inplace=True)


def tx_retorno(dataset):
    return (dataset / dataset.shift(1)) - 1


def tx_risco(dataset, pesos):
    tx_ret_anual = (tx_retorno(dataset).cov()) * 246
    m_result = np.dot(tx_ret_anual, pesos)
    variancia = np.dot(m_result, pesos)
    volatividade = math.sqrt(variancia)

    print(f"Variância: {variancia}\nVolatividade: {volatividade}")


pesos = np.array([0.2, 0.2, 0.2, 0.2, 0.2, 0.0])

tx_risco(base_acoes, pesos)
