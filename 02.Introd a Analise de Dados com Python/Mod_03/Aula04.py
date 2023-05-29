# Aula 04 - Leitura de Base de Dados de Ações Financeiras Online

import yfinance as yf  # Biblioteca para acessar dados financeiros do Yahoo Finance
from pandas_datareader import data

# Bibliotecas que serão utilizadas no modulo
"""import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt"""

# Ativa a função de substituição do pandas_datareader
yf.pdr_override()

# Define o símbolo da ação e a data de início
simbolo = "AZUL4.SA"
start = "2017-01-01"

# Obtém os dados do Yahoo Finance usando a função get_data_yahoo
azul_df = data.get_data_yahoo(simbolo, start)
print(azul_df)  # Imprime os dados
