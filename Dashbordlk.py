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

df_invite = pd.read_csv("Invitations.csv")
df_invite["Sent At"] = pd.to_datetime(df_invite["Sent At"], format="%m/%d/%y, %I:%M %p", errors='coerce')


df_react = pd.read_csv("Reactions.csv")
df_react["Date"] = pd.to_datetime(df_react["Date"], format="%m/%d/%Y %H:%M")
df_react["month"] = df_react['Date'].dt.month
df_react['month'] = df_react['month'].apply(lambda x: calendar.month_abbr[x])

df_msg = pd.read_csv("messages.csv")
df_msg["DATE"] = pd.to_datetime(df_msg["DATE"])



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
                    date=date(2021, 2, 15),
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
                    html.H6('Invites Send'),
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
    dff_c = df_cnt.copy()         # Connections
    dff_c = dff_c[(dff_c['Connected On']>=start_date) & (dff_c['Connected On']<=end_date)]
    conctns_num = len(dff_c)
    compns_num = len(dff_c['Company'].unique())

    dff_i = df_invite.copy()       # Invitations
    dff_i = dff_i[(dff_i['Sent At']>=start_date) & (dff_i['Sent At']<=end_date)]
   
    in_num = len(dff_i[dff_i['Direction'] == 'INCOMING'])     # print(dff_i)
    out_num = len(dff_i[dff_i['Direction'] == 'OUTGOING'])

    dff_r = df_react.copy()      # Reactions
    dff_r = dff_r[(dff_r['Date']>=start_date) & (dff_r['Date']<=end_date)]
    reactns_num = len(dff_r)

    return conctns_num, compns_num, in_num,out_num,reactns_num

 # Line Chart ***********************************************************
@app.callback(
    Output('line-chart', 'figure'),
    Input('my-date-picker-start', 'date'),
    Input('my-date-picker-end', 'date'),
)
def update_line(start_date, end_date):
    dff = df_cnt.copy()
    dff = dff[(dff['Connected On'] >= start_date) & (dff['Connected On'] <= end_date)]
    dff = dff["month"].value_counts().reset_index()
    dff.columns = ['month', 'Total connections']

    fig_line = px.line(dff, x='month', y='Total connections', template='ggplot2',
                       title="Total Connections by Month Name")
    fig_line.update_traces(mode="lines+markers", fill='tozeroy', line={'color': 'blue'})
    fig_line.update_layout(margin=dict(l=20, r=20, t=30, b=20))

    return fig_line


 #***************************************** Bar chart 
@app.callback(                               
    Output('bar-chart', 'figure'),
    Input('my-date-picker-start', 'date'),
    Input('my-date-picker-end', 'date'),
)
def update_bar(start_date, end_date):
    dff = df_cnt.copy()
    dff = dff[(dff['Connected On'] >= start_date) & (dff['Connected On'] <= end_date)]

    # Exclude 'NIL' values
    dff = dff[dff['Company'] != 'NIL']

    dff_grouped = dff.groupby('Company').size().reset_index(name='Total connections')

    # Select the top 10 companies
    dff_grouped = dff_grouped.sort_values(by='Total connections', ascending=False).head(10)

    fig_bar = px.bar(dff_grouped, x='Total connections', y='Company', template='ggplot2',
                     orientation='h', title="Top 10 Companies by Total Connections")
    fig_bar.update_yaxes(tickangle=45)
    fig_bar.update_layout(margin=dict(l=20, r=20, t=30, b=20))
    fig_bar.update_traces(marker_color='blue')

    return fig_bar

# Pie Chart ************************************************************
@app.callback(
    Output('pie-chart', 'figure'),
    Input('my-date-picker-start', 'date'),
    Input('my-date-picker-end', 'date'),
)
def update_pie(start_date, end_date):
    dff = df_msg.copy()
    dff = dff[(dff['DATE'] >= start_date) & (dff['DATE'] <= end_date)]

    msg_sent = len(dff[dff['FROM'] == 'Pranav Anandraj'])
    msg_rcvd = len(dff[dff['FROM'] != 'Pranav Anandraj'])

    fig_pie = px.pie(
        names=['Sent', 'Received'],
        values=[msg_sent, msg_rcvd],
        template='ggplot2',
        title="Messages Sent & Received"
    )
    
    fig_pie.update_layout(margin=dict(l=20, r=20, t=30, b=20))
    fig_pie.update_traces(marker_colors=['red', 'blue'])

    return fig_pie

# **************************************************** WordCloud

@app.callback(
    Output('wordcloud', 'figure'),
    Input('my-date-picker-start', 'date'),
    Input('my-date-picker-end', 'date'),
)
def update_wordcloud(start_date, end_date):
    dff = df_cnt.copy()
    dff = dff[(dff['Connected On'] >= start_date) & (dff['Connected On'] <= end_date)]
    
    # Remove occurrences of "NIL" in the 'Position' column
    dff = dff[dff['Position'] != 'NIL']

    positions = dff['Position'].astype(str)

    my_wordcloud = WordCloud(
        background_color='white',
        height=275
    ).generate_from_text(' '.join(positions))

    fig_wordcloud = px.imshow(my_wordcloud, template='ggplot2',
                              title="Word Cloud of Positions")
    fig_wordcloud.update_layout(margin=dict(l=20, r=20, t=30, b=20))
    fig_wordcloud.update_xaxes(visible=False)
    fig_wordcloud.update_yaxes(visible=False)

    return fig_wordcloud

#*********************************************TBD
@app.callback(
    Output('TBD', 'figure'),
    Input('my-date-picker-start', 'date'),
    Input('my-date-picker-end', 'date'),
)

def update_TBD(start_date,end_date):
              dff= df_react.copy()
              dff = dff[(dff['Date'] >= start_date) & (dff['Date'] <= end_date)]
              dff = dff["month"].value_counts().reset_index()
              dff.columns = ['month', 'Total Reaction']
              fig_line = px.line(dff, x='month', y='Total Reaction', template='ggplot2',
                   title="Total Reactions by Month Name")
              fig_line.update_traces(mode="lines+markers", fill='tozeroy', line={'color': 'blue'})
              fig_line.update_layout(margin=dict(l=20, r=20, t=30, b=20))
              
              return fig_line
    
if __name__=='__main__':
    app.run_server(debug=False, port=8002)
    
    
  