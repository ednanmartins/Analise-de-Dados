# Aula 33 - Calculando Risco de um Portfólio com Duas Ações
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

# TODO: taxas_retorno.columns.isin(ame_cvc)] seleciona todas as linhas (:)
# TODO: e apenas as colunas cujos rótulos estão presentes na lista ame_cvc.
tx_ret_ame_cvc = taxas_retorno.loc[:, taxas_retorno.columns.isin(ame_cvc)]
tx_ret_wege_magalu = taxas_retorno.loc[:, taxas_retorno.columns.isin(wege_magalu)]
tx_ret_via_bova = taxas_retorno.loc[:, taxas_retorno.columns.isin(via_bova)]

# ? Matrizes de Covariância Anual
cov_anual_ame_cvc = tx_ret_ame_cvc.cov() * 246
cov_anual_wege_magalu = tx_ret_wege_magalu.cov() * 246
cov_anual_via_bova = tx_ret_via_bova.cov() * 246

# ? Pesos
pesos = np.array([0.5, 0.5])

# * ============================================================================
# * ============================================================================

# ? Calculo de Risco de Portfólio (Forma maior) - AMERICANAS e CVC
matriz_resultante_ame_cvc = np.dot(cov_anual_ame_cvc, pesos)
variancia_ame_cvc = np.dot(pesos, matriz_resultante_ame_cvc)
desvio_padrao_ame_cvc = math.sqrt(variancia_ame_cvc)
desvio_padrao_ame_cvc

# ? Calculo de Risco de Portfólio (Forma maior) - WEGE e MAGALU
matriz_resultante_wege_magalu = np.dot(cov_anual_wege_magalu, pesos)
variancia_wege_magalu = np.dot(matriz_resultante_wege_magalu, pesos)
desvio_padrao_wege_magalu = math.sqrt(variancia_wege_magalu)
desvio_padrao_wege_magalu

# ? Calculo de Risco de Portfólio (Forma maior) - VIA e BOVA
matriz_resultante_via_bova = np.dot(cov_anual_via_bova, pesos)
variancia_via_bova = np.dot(matriz_resultante_via_bova, pesos)
desvio_padrao_via_bova = math.sqrt(variancia_via_bova)
desvio_padrao_via_bova
