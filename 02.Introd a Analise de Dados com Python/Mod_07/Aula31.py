# Aula 31 - Preparação para Cálculo de Risco de um Portfólio
"""# * Verde
# ! Vermelho
# ? Duvida
# TODO: Destaque"""

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
tx_ret_ame_cvc.cov() * 246
tx_ret_wege_magalu.cov() * 246
tx_ret_via_bova.cov() * 246

# ? Pesos
pesos = np.array([0.5, 0.5])
