# Aula 29 - Risco Médio Anual
"""# * Verde
# ! Vermelho
# ? Duvida
# TODO: Destaque"""

import math
import pandas as pd

base_acoes = pd.read_csv(
    "F:/Meus Documentos/Ednan Martins/Área de Trabalho/Ednan Pro/Cursos/Analise de Dados/02.Introd a Analise de Dados com Python/Mod_03/acoes.csv"
)
base_acoes.drop(labels=["Date"], axis=1, inplace=True)


""" Calcula as taxas de retorno utilizando a fórmula (valor atual / valor anterior) - 1.
O método shift(1) desloca os valores uma posição para cima, para calcular
a variação percentual entre valores consecutivos."""
taxas_retorno = (base_acoes / base_acoes.shift(1)) - 1

""" Calcula o desvio padrão das taxas de retorno e multiplica por 100.
Essa operação retorna o desvio padrão em termos percentuais."""
taxas_retorno.std() * 100


""" Calcula o desvio padrão das taxas de retorno e multiplica por 246.
Essa operação é comum para anualizar o desvio padrão quando há 246
diasúteis em um ano."""
taxas_retorno.std() * 246

""" Calcula o desvio padrão das taxas de retorno e multiplica pela
raiz quadrada de 246 utilizando a função math.sqrt(246). Essa operação
também tem o objetivo de anualizar o desvio padrão."""
taxas_retorno.std() * math.sqrt(246)
