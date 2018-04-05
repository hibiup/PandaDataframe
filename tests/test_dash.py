from unittest import TestCase

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from sklearn.metrics import roc_curve

class TestDash(TestCase):
    def test_dash(self):
        app = dash.Dash()

        app.layout = lambda: self.generate_html()

        app.run_server(host="0.0.0.0", debug=True)
    
    def generate_html(self):
        df_roc = pd.read_csv('tests/data/dashboard_data.csv')

        colors = {
            'background': '#111111',
            'text': 'black'
        }

        return html.Div([
            html.H1(
                children='One-Click Deployment Dashboard',
                style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
            ),

            html.Div(children=' Positive Recall', style={
                'textAlign': 'center',
                'color': colors['text']
            }),


            dcc.Graph(
                id='standard',
                figure={
                    'data': [
                        go.Scatter(
                            x = df_roc['fpr'],
                            y = df_roc['tpr'],
                            mode='lines',
                            opacity=0.5,
                            marker={
                                'size': 4,
                                'line': {'width': 1, 'color': 'black'}
                            },
                        ),
                        go.Scatter(
                            x = [0,1],
                            y = [0,1],
                            mode='lines',
                            opacity=0.5,
                            marker={
                                'size': 4,
                                'line': {'width': 1, 'color': 'black'}
                            },
                        ) 
                    ],
                    'layout': go.Layout(
                        xaxis={'title': 'True Positive Rate'},
                        yaxis={'title': 'False Positive Rate'},
                        legend={'x': 0, 'y': 1},
                        title='roc-curve',
                        height= 500,
                        width = 500,
                        hovermode='closest'
                    )
                }
            )
        ])