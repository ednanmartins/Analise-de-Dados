# Aula 28 - Implementando Coeficiente de Variação

import numpy as np
from scipy import stats


# Pode ser substituido por 'status.variation()*100'  --> status.variation(taxas)*100
# para isso, precisamos importar o pacote stats da biblioteca scipy
def calc_coeficiente_de_variacao(taxas):
    desvio_padrao = taxas.std()
    media = taxas.mean()
    return (desvio_padrao / media) * 100


taxas_ame = np.array([-36.32, -35.11, 72.17, 74.24, 39.14, 14.84, -86.74, 9.65])
taxas_cvc = np.array([-11.86, 63.73, 74.52, 20.42, -33.29, -77.59, -40.75, -105.30])
taxas_wege = np.array([-2.97, 5.71, 46.79, -9.28, 65.63, 76.51, -12.34, 18.46, 38.51])
taxas_magalu = np.array([-121.69, 177.75, 184.21, 82.56, 71.87, 70.46, -125.00, -89.71])
taxas_via = np.array([-151.15, 109.86, 73.57, -56.32, 93.62, 32.04, -112.49, -73.00])
taxas_bova = np.array([-11.49, 34.86, 0, 11.91, 23.54, 1.14, -12.38, 5.85])

coeficiente_de_variacao_ame = calc_coeficiente_de_variacao(taxas_ame)
coeficiente_de_variacao_cvc = calc_coeficiente_de_variacao(taxas_cvc)
coeficiente_de_variacao_wege = calc_coeficiente_de_variacao(taxas_wege)
coeficiente_de_variacao_magalu = calc_coeficiente_de_variacao(taxas_magalu)
coeficiente_de_variacao_via = calc_coeficiente_de_variacao(taxas_via)
coeficiente_de_variacao_bova = calc_coeficiente_de_variacao(taxas_bova)


# FORMA SIMPLIFICADA DE COMPARAR DESVIO PADRAO
coeficiente_simplificado_ame = stats.variation(taxas_ame) * 100
coeficiente_simplificado_cvc = stats.variation(taxas_cvc) * 100
coeficiente_simplificado_wege = stats.variation(taxas_wege) * 100
coeficiente_simplificado_magalu = stats.variation(taxas_magalu) * 100
coeficiente_simplificado_via = stats.variation(taxas_via) * 100
coeficiente_simplificado_bova = stats.variation(taxas_bova) * 100
