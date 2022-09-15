from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# O primeiro passo é construir o layout

# Dataframe como Base de dados. Lendo a base omo arquivo excel.
df = pd.read_excel("Vendas.xlsx")


# Posso construir o layout com html ou itens dcc(itens de dashoboards)
# Criando o gráfico com base no arquivo excel importado.
# O alias px do plotly + o .bar, significa gráfico de barra
# Para criar outro gráfico basta criar outra fig. E outro dcc.Graph com outro id
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
# Pegando todas as opções lojas do ID Loja para uma lista python
# unique para trazer valores distintos
opcoes = list(df['ID Loja'].unique())
# Quero também adcionar uma opção todas as lojas
opcoes.append('Todas as Lojas')
# Após criar a lista de opções preciso vincular ao botão de opções (dcc.Dropdown) criado anteriormente

# Construindo uma lista de itens
# Parâmetro children para construção de textos em dash html
app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.H2(children='Gráficos com produtos separados por loja: '),
    #html.Link quero acrescentar o link do meu Linkedin
    html.Div(children='''
        Gráfico com a quantidade de produtos vendidos.
    '''),
    # O div abaixo foi criado só para testar o callback, processo realizado anteriormente ao do div acima
    # html.Div(id='texto'),
# Criando um botão dropddown
# Lembrar sempre de colocar a vírgula, pois se trata de uma lista de itens. O único que não é preciso fazer isso, é o último item.
# Quero exibir neste botão as opções de lojas da minha base de dados
# Value mostra o valor inicial do botão
    dcc.Dropdown(opcoes, value='Todas as Lojas', id='lista_lojas'),
# Criando o gráfico conforme a variável fig criada anteriormente
    dcc.Graph(
        id='grafico_qtde_vendas',
        figure=fig
    )
])

# Callback indica quais são as coisas que serão modificadas de forma dinâmica. E como elas serão modificadas de forma dinâmica.
# Sempre que utilizar o callback, importar Input e Output.
# Imput, indica quem vai selecionar o valor
# Output, indica oq será modificado / editado
# O primeiro parâmetro é o id
# A segunda informação a ser passada no input e no output é o parâmetro que quero alterar
# Se eu quiser editar o texto de uma div tenho que editar o parâmetro children
@app.callback(
    Output('grafico_qtde_vendas', 'figure'),
    Input('lista_lojas', 'value')
)
def update_output(value):
# Criando a condição para exibir o gráfico com os valores de todas as lojas
# Else para exibição dos valores de lojas únicas
# .loc realiza o filtro [linhas, colunas] se eu quiser todas as colunas só apresentar conforme o laço abaixo
# Quero filtrar as linhas cujo valor corresponde. Ou seja, quero pegar as linhas onde a coluna ID Loja é igual a loja que estou selecionando no botão
# O fig no else, ao invés de utilizar a tabela toda, indico que será a tabela com linha filtrada
    if value == "Todas as Lojas":
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Loja'] == value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig
# Essa função agora recebe o parâmetro do dropdow e ela retorna a informação que é a variável que armazena o gráfico
    #return f'Loja Selecionada: {value}'

# Resumindo, o callback é um decorator que atribui uma nova funcionalidade. Neste caso ao def acima
# A função def update_output obrigatoriamente tem que receber o parêmetro do Input. Essa função retorna quem quero colocar no Output.
# Resumindo essa função conecta as duas coisas do decorator
# Em amarelo na função é o texto de retorno

# Cod. Para rodar o server
if __name__ == '__main__':
    app.run_server(debug=True)
