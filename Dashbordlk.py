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

# Lottie animations links *************************************************
url_coonections = "https://assets9.lottiefiles.com/private_files/lf30_5ttqPi.json"
url_companies = "https://assets9.lottiefiles.com/packages/lf20_EzPrWM.json"
url_msg_in = "https://assets9.lottiefiles.com/packages/lf20_8wREpI.json"
url_msg_out = "https://assets2.lottiefiles.com/packages/lf20_Cc8Bpg.json"
url_reactions = "https://assets2.lottiefiles.com/packages/lf20_nKwET0.json"
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

# Import App data from csv sheets **************************************
df_cnt = pd.read_csv("Connections.csv")
df_cnt["Connected On"] = pd.to_datetime(df_cnt["Connected On"])
df_cnt["month"] = df_cnt["Connected On"].dt.month
df_cnt['month'] = df_cnt['month'].apply(lambda x: calendar.month_abbr[x])


# Bootstrap themes by Ann: https://hellodash.pythonanywhere.com/theme_explorer
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = dbc.Container([
dbc.Row([  # Row 1 with 2 col
    dbc.Col([
        dbc.Card([
            dbc.CardImg(src='./assets/linkedin-logo2.png')  # social media logo image
        ], className='mb-2'),
        dbc.Card([
            dbc.CardBody([
                dbc.CardLink("Nandakishor V", target="_blank",  # Link to the resume / Dash component 1
                             href="https://drive.google.com/file/d/1RnodqYH0kgT0RiG-WGA5yqs745E6HEgr/view?usp=drive_link"
                             )
            ])
        ]),
    ], width=2),
    dbc.Col([
        dbc.Card([
            dbc.CardBody([  # DCC Datapicker single
                dcc.DatePickerSingle(
                    id='my-date-picker-start',
                    date=date(2021, 3, 15),
                    className='ml-5'
                ),
                dcc.DatePickerSingle(
                    id='my-date-picker-end',
                    date=date(2024, 2, 24),
                    style={'margin-left': '10px', 'margin-top': '10px'}  # Adjusted using style instead of className className not working 
                ),
            ]),
        ], color="info"),
    ], width=8),
], className='mb-2 mt-3'),
   dbc.Row([                                                               # Row 2 with 5 col
    dbc.Col([
        dbc.Card([
            dbc.CardBody([
                dbc.CardHeader(Lottie(options=options, style={'width': '60px', 'height': '60px'}, url=url_coonections)),
                dbc.CardBody([
                    html.H6('Connections'),
                    html.H2(id='content-connections', children="000")
                ], style={'textAlign': 'center'})
            ])
        ]),
    ], width=2),
    dbc.Col([
        dbc.Card([
            dbc.CardBody([
                dbc.CardHeader(Lottie(options=options, style={'width': '60px', 'height': '60px'}, url=url_companies)),
                dbc.CardBody([
                    html.H6('Companies'),
                    html.H2(id='content-companies', children="000")
                ], style={'textAlign': 'center'})
            ])
        ]),
    ], width=2),
    dbc.Col([
        dbc.Card([
            dbc.CardBody([
                dbc.CardHeader(Lottie(options=options, style={'width': '60px', 'height': '60px'}, url=url_msg_in)),
                dbc.CardBody([
                    html.H6('Invites Received'),
                    html.H2(id='content-msg_in', children="000")
                ], style={'textAlign': 'center'})
            ])
        ]),
    ], width=2),
    dbc.Col([
        dbc.Card([
            dbc.CardBody([
                dbc.CardHeader(Lottie(options=options, style={'width': '60px', 'height': '60px'}, url=url_msg_out)),
                dbc.CardBody([
                    html.H6('Messages Send'),
                    html.H2(id='content-msg_out', children="000")
                ], style={'textAlign': 'center'})
            ])
        ]),
    ], width=2),
    dbc.Col([
        dbc.Card([
            dbc.CardBody([
                dbc.CardHeader(Lottie(options=options, style={'width': '60px', 'height': '60px'}, url=url_reactions)),
                dbc.CardBody([
                    html.H6('Reactions'),
                    html.H2(id='content-reactions', children="000")
                ], style={'textAlign': 'center'})
            ])
        ]),
    ], width=2),
], className='mb-2'),
  dbc.Row([                                     #Row 3 col 2
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='line-chart', figure={}),  #line chart
                ])
            ]),
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='bar-chart', figure={}),  #bar chart
                ])
            ]),
        ], width=4),
    ],className='mb-2'),
    dbc.Row([               # Row 4  col 3
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='TBD', figure={}),     # TBD
                ])
            ]),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='pie-chart', figure={}),       # pie chart
                ])
            ]),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='wordcloud', figure={}),   # wordcloud
                ])
            ]),
        ], width=4),
    ],className='mb-2'),
], fluid=True)


@app.callback(  # Updating the 5 number cards in row 2
    Output('content-connections', 'children'),
    Output('content-companies', 'children'),
    Output('content-msg_in', 'children'),  
    Output('content-msg_out', 'children'),
    Output('content-reactions', 'children'),
    Input('my-date-picker-start', 'date'),
    Input('my-date-picker-end', 'date'),
)
def update_small_cards(start_date, end_date):
    dff_c = df_cnt.copy()  # Connections
    dff_c = dff_c[(dff_c['Connected On'] >= start_date) & (dff_c['Connected On'] <= end_date)]
    conctns_num = len(dff_c)
    compns_num = len(dff_c['Company'].unique())
    return conctns_num, compns_num, 0, 0, 0  

    
if __name__=='__main__':
    app.run_server(debug=False, port=8002)
    
    
  