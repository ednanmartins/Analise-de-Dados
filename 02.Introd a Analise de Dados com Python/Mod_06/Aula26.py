# Aula 26 - Implementando o Desvio Padrão

import math
import pandas as pd
import numpy as np

base_acoes = pd.read_csv(
    "F:/Meus Documentos/Ednan Martins/Área de Trabalho/Ednan Pro/Cursos/Analise de Dados/02.Introd a Analise de Dados com Python/Mod_03/acoes.csv"
)


# Pode ser substituido por '.std()'  --> taxas.std()
def calc_desvio_padrao(taxas):
    variancia = taxas.var()
    return math.sqrt(variancia)


taxas_ame = np.array([-36.32, -35.11, 72.17, 74.24, 39.14, 14.84, -86.74, 9.65])
taxas_cvc = np.array([-11.86, 63.73, 74.52, 20.42, -33.29, -77.59, -40.75, -105.30])
taxas_wege = np.array([-2.97, 5.71, 46.79, -9.28, 65.63, 76.51, -12.34, 18.46, 38.51])
taxas_magalu = np.array([-121.69, 177.75, 184.21, 82.56, 71.87, 70.46, -125.00, -89.71])
taxas_via = np.array([-151.15, 109.86, 73.57, -56.32, 93.62, 32.04, -112.49, -73.00])
taxas_bova = np.array([-11.49, 34.86, 0, 11.91, 23.54, 1.14, -12.38, 5.85])

desvio_padrao_ame = calc_desvio_padrao(taxas_ame)
desvio_padrao_cvc = calc_desvio_padrao(taxas_cvc)
desvio_padrao_wege = calc_desvio_padrao(taxas_wege)
desvio_padrao_magalu = calc_desvio_padrao(taxas_magalu)
desvio_padrao_via = calc_desvio_padrao(taxas_via)
desvio_padrao_bova = calc_desvio_padrao(taxas_bova)

# FORMA SIMPLIFICADA DE COMPARAR DESVIO PADRAO
base_acoes["AMERICANAS"].tail(30).std()  # Desvio Padrao dos ultimos 30D
base_acoes["MAGALU"].tail(30).std()  # Desvio Padrao dos ultimos 30D
