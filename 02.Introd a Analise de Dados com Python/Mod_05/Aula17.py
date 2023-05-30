# Aula 17 - Verificando Taxa de Retorno Logarítmica

import numpy as np
import pandas as pd

# import seaborn as sns
# import yfinance as yf  # Biblioteca para acessar dados financeiros do Yahoo Finance
# import plotly.express as px
# import matplotlib.pyplot as plt
# from pandas_datareader import data

dataset = pd.read_csv(
    "F:/Meus Documentos/Ednan Martins/Área de Trabalho/Ednan Pro/Cursos/Analise de Dados/02.Introd a Analise de Dados com Python/Mod_03/acoes.csv"
)
# print(dataset)

# Um pequeno ajuste tecnico pra Americanas não ficar com linha quebrada
ult = len(dataset) - 1

# CALCULO DA TAXA DE RETORNO LOGARÍTMICA
rl_americanas = np.log(dataset["AMERICANAS"][ult] / dataset["AMERICANAS"][0]) * 100
rl_cvc = np.log(dataset["CVC"][len(dataset) - 1] / dataset["CVC"][0]) * 100
rl_wege = np.log(dataset["WEGE"][len(dataset) - 1] / dataset["WEGE"][0]) * 100
rl_magalu = np.log(dataset["MAGALU"][len(dataset) - 1] / dataset["MAGALU"][0]) * 100
rl_via = np.log(dataset["VIA"][len(dataset) - 1] / dataset["VIA"][0]) * 100
rl_bova = np.log(dataset["BOVA"][len(dataset) - 1] / dataset["BOVA"][0]) * 100
