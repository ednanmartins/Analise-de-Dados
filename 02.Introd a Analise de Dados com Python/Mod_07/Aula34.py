# Aula 34 - Calculando Risco de Várias Ações
"""# * Verde
# ! Vermelho
# ? Duvida
# TODO: Destaque"""

import math
import numpy as np
import pandas as pd

base_acoes = pd.read_csv(
    "F:/Meus Documentos/Ednan Martins/Área de Trabalho/Ednan Pro/Cursos/Analise de Dados/02.Introd a Analise de Dados com Python/Mod_03/acoes.csv"
)
base_acoes.drop(labels=["Date"], axis=1, inplace=True)

acoes = ["AMERICANAS", "CVC", "WEGE", "MAGALU", "VIA", "BOVA"]
ame_cvc = ["AMERICANAS", "CVC"]
wege_magalu = ["WEGE", "MAGALU"]
via_bova = ["VIA", "BOVA"]

# ? Taxa de Retorno
taxas_retorno = (base_acoes / base_acoes.shift(1)) - 1

# ? Todas Ações
pesos1 = np.array([0.2, 0.2, 0.2, 0.2, 0.2, 0.0])
tx_anual = taxas_retorno.cov() * 246
m_result = np.dot(tx_anual, pesos1)
variancia_port1 = np.dot(m_result, pesos1)
volatividade_port1 = math.sqrt(variancia_port1)

print(variancia_port1)
print(volatividade_port1)
print("==========================")

# ? Comparação com BOVA
pesos2 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 1.0])
variancia_port2 = np.dot(m_result, pesos2)
volatividade_port2 = math.sqrt(variancia_port2)

print(variancia_port2)
print(volatividade_port2)
print("==========================")
