from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# O primeiro passo é construir o layout

# Dataframe como Base de dados
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
# Posso construir o layout com html ou itens dcc(itens de dashoboards)
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

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)