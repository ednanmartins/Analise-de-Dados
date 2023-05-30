# Aula 13 - Verificando Taxa de Retorno Simples

# import numpy as np
import pandas as pd

# import seaborn as sns
# import yfinance as yf  # Biblioteca para acessar dados financeiros do Yahoo Finance
# import plotly.express as px
# import matplotlib.pyplot as plt
# from pandas_datareader import data

dataset = pd.read_csv(
    "F:/Meus Documentos/Ednan Martins/Área de Trabalho/Ednan Pro/Cursos/Analise de Dados/02.Introd a Analise de Dados com Python/Mod_03/acoes.csv"
)

# print(dataset.shape)
# dataset

# dataset["AMERICANAS"][0]  # Printa linha 0
# dataset["AMERICANAS"][len(dataset) - 1]  # Printa tamanho do dataset -1 (ultima linha)


# FORMATO TRADICIONAL
rs_americanas = (
    (dataset["AMERICANAS"][len(dataset) - 1] - dataset["AMERICANAS"][0])
    / dataset["AMERICANAS"][0]
) * 100

rs_cvc = (
    (dataset["CVC"][len(dataset) - 1] - dataset["CVC"][0]) / dataset["CVC"][0]
) * 100

rs_wege = (
    (dataset["WEGE"][len(dataset) - 1] - dataset["WEGE"][0]) / dataset["WEGE"][0]
) * 100

rs_magalu = (
    (dataset["MAGALU"][len(dataset) - 1] - dataset["MAGALU"][0]) / dataset["MAGALU"][0]
) * 100

rs_via = (
    (dataset["VIA"][len(dataset) - 1] - dataset["VIA"][0]) / dataset["VIA"][0]
) * 100

rs_bova = (
    (dataset["BOVA"][len(dataset) - 1] - dataset["BOVA"][0]) / dataset["BOVA"][0]
) * 100

print("Retorno Simples Americanas: ", rs_americanas)
print("Retorno Simples Cvc: ", rs_cvc)
print("Retorno Simples Wege: ", rs_wege)
print("Retorno Simples Magalu: ", rs_magalu)
print("Retorno Simples Via: ", rs_via)
print("Retorno Simples Bova: ", rs_bova, "\n\n")

# FORMA REDUZIDA
rs_americanas_fr = (
    dataset["AMERICANAS"][len(dataset) - 1] / dataset["AMERICANAS"][0] - 1
) * 100

rs_cvc_fr = (dataset["CVC"][len(dataset) - 1] / dataset["CVC"][0] - 1) * 100

rs_wege_fr = (dataset["WEGE"][len(dataset) - 1] / dataset["WEGE"][0] - 1) * 100

rs_magalu_fr = (dataset["MAGALU"][len(dataset) - 1] / dataset["MAGALU"][0] - 1) * 100

rs_via_fr = (dataset["VIA"][len(dataset) - 1] / dataset["VIA"][0] - 1) * 100

rs_bova_fr = (dataset["BOVA"][len(dataset) - 1] / dataset["BOVA"][0] - 1) * 100

print("Retorno Simples Americanas (Forma Reduzida): ", rs_americanas_fr)
print("Retorno Simples Americanas (Forma Reduzida): ", rs_cvc_fr)
print("Retorno Simples Americanas (Forma Reduzida): ", rs_wege_fr)
print("Retorno Simples Americanas (Forma Reduzida): ", rs_magalu_fr)
print("Retorno Simples Americanas (Forma Reduzida): ", rs_via_fr)
print("Retorno Simples Americanas (Forma Reduzida): ", rs_bova_fr)
