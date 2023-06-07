# Aula 30 - Covariância e Coeficiente de Correlação
"""# * Verde
# ! Vermelho
# ? Duvida
# TODO: Destaque"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

base_acoes = pd.read_csv(
    "F:/Meus Documentos/Ednan Martins/Área de Trabalho/Ednan Pro/Cursos/Analise de Dados/02.Introd a Analise de Dados com Python/Mod_03/acoes.csv"
)
base_acoes.drop(labels=["Date"], axis=1, inplace=True)

# ? Taxa de Retorno
taxas_retorno = (base_acoes / base_acoes.shift(1)) - 1

# ? Covariância
""" >0, variáveis se movem juntas
    <0, variáveis se movem em direções opostas
    =0, variáveis são independentes"""
taxas_retorno.cov()

# ? Correlação
taxas_retorno.corr()

plt.figure(figsize=(8, 8))

# TODO: 'annot=True' exibe info/legenda dentro do proprio grafico
sns.heatmap(taxas_retorno.corr(), annot=True)
