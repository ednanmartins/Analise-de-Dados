# Aula 22 - Taxas de Retorno Por Ano
# RAPAZ, NESSA AULA EU VOEEI VIU, KKK. Q CODIGO LINDO MEUS ZAMIGU

import pandas as pd
import numpy as np

# Biblioteca para se referenciar a dias úteis
from pandas.tseries.offsets import CustomBusinessDay

"""BIBLIOTECAS DO MODULO
import math
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats"""

base_acoes = pd.read_csv(
    "F:/Meus Documentos/Ednan Martins/Área de Trabalho/Ednan Pro/Cursos/Analise de Dados/02.Introd a Analise de Dados com Python/Mod_03/acoes.csv"
)

lista_acoes = ["AMERICANAS", "CVC", "WEGE", "MAGALU", "VIA", "BOVA"]
anos = ["2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]


def calc_dias_uteis(ano):
    calend = pd.DataFrame(index=pd.date_range(start=f"{ano}-01-01", end=f"{ano}-12-31"))
    dias_uteis = CustomBusinessDay()
    pri_dUtil = (calend.index[0] + dias_uteis).date()
    ult_dUtil = (calend.index[-1] - dias_uteis).date()

    return pri_dUtil, ult_dUtil


def calc_tr_anual(dataset, coluna, ano):
    # DIAS UTEIS:
    pri_dUtil, ult_dUtil = calc_dias_uteis(ano)

    # TRATAMENTO DE DATAS:
    if str(pri_dUtil) in dataset["Date"].values:
        val_inicial = dataset[coluna][dataset["Date"] == str(pri_dUtil)].values[0]
    else:
        pri_dUtil += pd.DateOffset(days=1)
        pri_dUtil = pri_dUtil.date()
        val_inicial = dataset[coluna][dataset["Date"] == str(pri_dUtil)].values[0]

    if str(ult_dUtil) in dataset["Date"].values:
        val_final = dataset[coluna][dataset["Date"] == str(ult_dUtil)].values[0]
    else:
        ult_dUtil -= pd.DateOffset(days=1)
        ult_dUtil = ult_dUtil.date()
        val_final = dataset[coluna][dataset["Date"] == str(ult_dUtil)].values[0]

    # CALCULO DE RETORNO LOGARITMICA:
    ret_log = np.log(val_final / val_inicial) * 100

    print(
        f"Taxa de Retorno Anual da {coluna} em {ano}:\n"
        f"Dt Inicial({pri_dUtil.strftime('%d/%m/%Y')}): {val_inicial:.2f}   /   "
        f"Dt Final({ult_dUtil.strftime('%d/%m/%Y')}): {val_final:.2f}\n"
        f"Portanto o Retorno Logaritmica ((Dt Fi/Dt In)*100) é de {ret_log:.2f}%"
    )


def verf_por_ano():
    ano = input("Me fale um ano entre 2015 e 2022: ")
    if ano in anos:
        for acao in lista_acoes:
            calc_tr_anual(base_acoes, acao, ano), print()
    else:
        print("Vish rapaz, esse ano aí num vale não!")


def verf_por_acao():
    acao = str(input("Me fale uma Ação ai pae: "))
    if acao in lista_acoes:
        for ano in anos:
            calc_tr_anual(base_acoes, acao, ano), print()
    else:
        print("Vish rapaz, tem essa empresa não!")


def menu():
    escolha = input(
        "Como gostaria de verificar?\n"
        "1- Verificar por Ano\n"
        "2- Verificar por Ação\n"
        "3- Sair\n\n"
        "Digite sua escolha: "
    )

    if escolha == "1" or escolha == "Ano":
        verf_por_ano()

    elif escolha == "2" or escolha == "Ação":
        verf_por_acao()

    elif escolha == "3" or escolha == "Sair":
        print("Então amigos. Terminou!")

    else:
        print("Naam, ta errado, tenta de novo meu fi!")
        menu()


menu()
