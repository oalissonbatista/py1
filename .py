############################################ BIBLIOTECAS UTILIZADAS ############################################

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px
import numpy as np

############################################ VARIÁVEIS UTILIZADAS ############################################

app = dash.Dash(__name__)
df = pd.read_csv("https://raw.githubusercontent.com/joaombc/APC2021/main/separado_por_estado.csv")
dados = df.values
print(dados)

'''
dados[:,0] #Estados
dados[:,1] #Jan 2020
dados[:,2] #Jan 2021
dados[:,3] #variação
'''

############################################ DADOS DO .CSV ############################################

t = dados[:,0] #Estados
v = dados[:,1] #Jan 2020
a = dados[:,2] #Jan 2021
b = dados[:,3] #Variação

############################################ LAYOUT HTML ############################################

app.layout = html.Div([
    html.H1("Fabrinilton", style=
    {
        'text-align': 'center'
    }),
    html.Div(id='output_container', children=[]),
    html.Br()
])

############################################ ATUALIZAÇÃO DOS GRÁFICOS ############################################

def update_graph():

        ############ INÍCIO DO GRÁFICO 1 ############

        trace = go.Scatter(
                x = t,
                y = b,
                mode = 'markers',
                name = 'Variação',
                marker =  
                {
                    'color' : '#000000',
                    'line' : 
                    {
                        'width': 1,
                        'color': '#000000'
                    }
                },
                opacity=.8)

        barra1 = go.Bar(
                x = t,
                y = v,
                name = 'Jan 2020',
                marker = 
                {
                    'color': '#29007f'
                }) ############ BARRA JAN/2020 ############

        barra2 = go.Bar(
                x = t,
                y = a,
                name = 'Jan 2021',
                marker = 
                {
                    'color': '#78002c'
                }) ############ BARRA JAN/2021 ############

        ############ TÉRMINO DO GRÁFICO 1 ############

        #################################################################################################################

        ############ INÍCIO DO GRÁFICO 2 ############

        linha = go.Scatter(
                x = t,
                y = b,
                mode = 'lines',
                name = 'Gráfico com linhas tracejadas',
                line = 
                {
                    'color': '#ee5253',
                    'dash': 'dash'
                }) ############ LINHA DO GRÁFICO ############

        pontos = go.Scatter(
                x = t,
                y = b,
                mode = 'markers',
                name = 'Variação',
                marker =  
                {
                    'color' : '#000000',
                    'line' : 
                    {
                        'width': 1,
                        'color': '#000000'
                    }
                },
                opacity=.8)  ############ PONTOS DO GRÁFICO ############

        ############ TÉRMINO DO GRÁFICO 2 ############
    
        #################################################################################################################

        ############ LAYOUT DOS GRÁFICOS ############

        layout = go.Layout(
                title = 'Movimento dos Estados',
                xaxis = 
                {
                    'title': 'Estados'
                },
                yaxis = 
                {
                    'title': 'Movimentação de passageiros'
                },
                xaxis_tickangle=-45)

        layout2 = go.Layout(
                title = 'Movimento dos Estados',
                xaxis = 
                {
                    'title': 'Estados'
                },
                yaxis = 
                {
                    'title': 'Variação (%)'
                },
                xaxis_tickangle=-45)

        ############ TÉRMINO DO LAYOUT ############

        #################################################################################################################

        ############ EXECUÇÃO DOS GRÁFICOS ############

        data = [barra1, barra2]
        fig = go.Figure(data=data, layout=layout)
        data2 = [linha, pontos]
        fig2 = go.Figure(data=data2, layout=layout2)
        return fig, fig2;

        ############ TÉRMINO DOS GRÁFICOS ############

#################################################################################################################

############################################ EXECUÇÃO DA DASHBOARD ############################################

if __name__ == '__main__':
    app.run_server(debug=True)

############################################ TÉRMINO DO CÓDIGO ############################################
