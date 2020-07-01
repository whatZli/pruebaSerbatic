import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from datetime import datetime as dt
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H3("Generico"),
    
])

if __name__ == "__main__":
    app.run_server(debug=True)


