from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# O primeiro passo é construir o layout

# Dataframe como Base de dados. Lendo a base omo arquivo excel.
df = pd.read_excel("Vendas.xlsx")


# Posso construir o layout com html ou itens dcc(itens de dashoboards)
# Criando o gráfico com base no arquivo excel importado.
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Construindo uma lista de itens
# Parâmetro children para construção de textos em dash html
app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.H2(children='Gráficos com produtos separados por loja: '),
    #html.Link quero acrescentar o link do meu Linkedin
    html.Div(children='''
        Gráfico com a quantidade de produtos vendidos.
    '''),
# Criando o gráfico conforme a variável fig criada anteriormente
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# Cod. Para rodar o server
if __name__ == '__main__':
    app.run_server(debug=True)