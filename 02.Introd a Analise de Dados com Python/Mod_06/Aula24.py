# Aula 24 - Implementando a Variância

import pandas as pd
import numpy as np

base_acoes = pd.read_csv(
    "F:/Meus Documentos/Ednan Martins/Área de Trabalho/Ednan Pro/Cursos/Analise de Dados/02.Introd a Analise de Dados com Python/Mod_03/acoes.csv"
)


# Pode ser substituido por '.mean()'  --> taxas.mean()
def calc_media(taxas):
    return taxas.sum() / len(taxas)


def calc_desvio(taxas):
    media = calc_media(taxas)
    return (taxas - media) ** 2


# Pode ser substituido por '.var()'  --> taxas.var()
def calc_variancia(taxas):
    desvio = calc_desvio(taxas)
    return (desvio.sum()) / len(taxas)


taxas_ame = np.array([-36.32, -35.11, 72.17, 74.24, 39.14, 14.84, -86.74, 9.65])
taxas_cvc = np.array([-11.86, 63.73, 74.52, 20.42, -33.29, -77.59, -40.75, -105.30])
taxas_wege = np.array([-2.97, 5.71, 46.79, -9.28, 65.63, 76.51, -12.34, 18.46, 38.51])
taxas_magalu = np.array([-121.69, 177.75, 184.21, 82.56, 71.87, 70.46, -125.00, -89.71])
taxas_via = np.array([-151.15, 109.86, 73.57, -56.32, 93.62, 32.04, -112.49, -73.00])
taxas_bova = np.array([-11.49, 34.86, 0, 11.91, 23.54, 1.14, -12.38, 5.85])

media_ame = calc_media(taxas_ame)
media_cvc = calc_media(taxas_cvc)
media_wege = calc_media(taxas_wege)
media_magalu = calc_media(taxas_magalu)
media_via = calc_media(taxas_via)
media_bova = calc_media(taxas_bova)

desvio_ame = calc_desvio(taxas_ame)
desvio_cvc = calc_desvio(taxas_cvc)
desvio_wege = calc_desvio(taxas_wege)
desvio_magalu = calc_desvio(taxas_magalu)
desvio_via = calc_desvio(taxas_via)
desvio_bova = calc_desvio(taxas_bova)

variancia_ame = calc_variancia(taxas_ame)
variancia_cvc = calc_variancia(taxas_cvc)
variancia_wege = calc_variancia(taxas_wege)
variancia_magalu = calc_variancia(taxas_magalu)
variancia_via = calc_variancia(taxas_via)
variancia_bova = calc_variancia(taxas_bova)


# MANEIRA SIMPLIFICADA DE PEGAR A VARIANCIA
base_acoes["AMERICANAS"].tail(30).var()  # Printa a variante dos ultimos 30D
base_acoes["MAGALU"].tail(30).var()  # Printa a variante dos ultimos 30D
