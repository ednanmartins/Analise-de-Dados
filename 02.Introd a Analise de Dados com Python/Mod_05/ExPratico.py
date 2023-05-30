""" EXERCICIO PRÁTICO

Usando a base de dados gerada no EXERÍCIO PRÁTICO da aula 14,
calcule as taxas de retorno desta carteira de ações e faça a comparação
da mesma através de um gráfico, com as ações da Bovespa.

De acordo com seu gráfico, qual é mais vantajosa de se investir, sua carteira de ações ou a BOVA11?

Justifique!"""

import pandas as pd
import plotly.express as px

acoes_bancos = pd.read_csv(
    "F:/Meus Documentos/Ednan Martins/Área de Trabalho/Ednan Pro/Cursos/Analise de Dados/02.Introd a Analise de Dados com Python/Mod_04/acoes_bancos.csv"
)

acoes_normalizado = acoes_bancos.copy()

for i in acoes_normalizado.columns[1:]:
    acoes_normalizado[i] = acoes_normalizado[i] / acoes_normalizado[i][0]

acoes_normalizado["CARTEIRA"] = (
    acoes_normalizado["BRADESCO"]
    + acoes_normalizado["BB"]
    + acoes_normalizado["NUBANK"]
    + acoes_normalizado["ITAÚ"]
    + acoes_normalizado["CAIXA"]
) / 5

figura = px.line(title="Compativo de Carteira (Ações Bancarias) com BOVA")
for i in acoes_normalizado.columns[1:]:
    figura.add_scatter(x=acoes_normalizado["Date"], y=acoes_normalizado[i], name=i)
figura.show()

acoes_normalizado.drop(
    ["BRADESCO", "BB", "NUBANK", "ITAÚ", "CAIXA"], axis=1, inplace=True
)

figura = px.line(title="Compativo de Carteira (Ações Bancarias) com BOVA")
for i in acoes_normalizado.columns[1:]:
    figura.add_scatter(x=acoes_normalizado["Date"], y=acoes_normalizado[i], name=i)
figura.show()
