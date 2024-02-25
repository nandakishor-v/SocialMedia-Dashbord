import dash
from dash import html, dcc
from dash.dependencies import Output, Input
from dash_extensions import Lottie
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from datetime import date
import calendar
from wordcloud import WordCloud



# Bootstrap themes by Ann: https://hellodash.pythonanywhere.com/theme_explorer
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = dbc.Container([
    dbc.Row([                                               # Row 1 with 2 col
        dbc.Col([
            dbc.Card([
             dbc.CardImg(src='./assets/linkedin-logo2.png') #social media logo image 
            ],className='mb-2'),
            dbc.Card([
                dbc.CardBody([
                     dbc.CardLink("Nandakishor V", target="_blank",
                                 href="https://drive.google.com/file/d/1RnodqYH0kgT0RiG-WGA5yqs745E6HEgr/view?usp=drive_link"
                    )
                ])
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=8),
    ],className='mb-2 mt-3'),
    dbc.Row([                                               # Row 2 with 5 col
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=2),
    ],className='mb-2'),
    dbc.Row([                                              # Row 3 with 2 col
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=4),
    ],className='mb-2'),
    dbc.Row([                                              # Row 4 with 3 col
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=4),
    ],className='mb-2'),
], fluid=True)



if __name__=='__main__':
    app.run_server(debug=False, port=8001)
