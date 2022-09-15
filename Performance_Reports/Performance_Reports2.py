import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

from dash import Dash, html, dcc, Input, Output
from plotly.subplots import make_subplots


app = Dash(__name__)

df = pd.read_csv("https://drive.google.com/file/d/1L8u0ORAGc_q4nEhRl1MPNe2ssoQe0ltB/view?usp=sharing")

fig = make_subplots(
    rows=3, cols=1,
    shared_xaxes=True,
    vertical_spacing=0.03,
    specs=[[{"type": "table"}],
           [{"type": "scatter"}],
           [{"type": "scatter"}]]
)

fig.add_trace(
    go.Table(
        header=dict(
            values=["requestedUrl", "Number<br>Transactions", "Output<br>Volume (BTC)",
                    "Market<br>Price", "Hash<br>Rate", "Cost per<br>trans-USD",
                    "teste<br>teste"],
            font=dict(size=10),
            align="left"
        ),
        cells=dict(
            values=[df["requestedUrl"].tolist() for k in df.columns[1:]],
            align = "left")
    ),
    row=1, col=1
)

# fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
#
# fig = make_subplots(
#     rows=3, cols=1,
#     shared_xaxes=True,
#     vertical_spacing=0.03,
#     specs=[[{"type": "table"}],
#            [{"type": "scatter"}],
#            [{"type": "scatter"}]]
# )

fig.show()

if __name__ == '__main__':
    app.run_server(debug=True)