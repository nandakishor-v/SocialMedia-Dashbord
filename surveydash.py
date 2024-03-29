import dash
from dash import html, dcc
from dash.dependencies import Output, Input
from dash_extensions import Lottie
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from datetime import date
from wordcloud import WordCloud 
import plotly.graph_objs as go




# Lottie animations links *************************************************

url_total="https://lottie.host/b52aedde-1a2c-4afa-a4c2-3c24d3914d14/PBMCZlWueD.json"
url_trauma="https://lottie.host/9d1250f2-c0cf-4ed7-b807-278d0ec5648d/YzpL4USg5O.json"
url_male="https://lottie.host/61179665-9ccb-49bf-9895-30c03b2f8c6c/FePWOgX91p.json"
url_female="https://lottie.host/947e9c27-4545-435a-8ffa-47f12b45cb3c/9GCO0scIeS.json"
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))


# Assuming the CSV file is in the same directory as your script
file_path = r"C:\Users\nanda\OneDrive\Desktop\repo\SocialMedia-Dashbord\Emotions(Responses).csv"

# Read the CSV file
df_cnt = pd.read_csv(file_path)

# Assuming the date column in your CSV file is in the format "mm/dd/yy, hh:mm AM/PM"
df_cnt["date"] = pd.to_datetime(df_cnt["date"], format="%d-%m-%Y %H:%M")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
               dbc.CardImg(src="/assets\logo.jpg")
            ],className='mb-2'),
            dbc.Card([
                dbc.CardBody([
                          dbc.CardLink("Know more about us", target="_blank",  # Link to the resume / Dash component 1
                             href="https://itch.io/profile/reflexbyte"
                             )
                ])
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
              dcc.DatePickerSingle(
                    id='my-date-picker-start',
                    date=date(2024, 3, 7),
                    className='ml-5'
                ),
                dcc.DatePickerSingle(
                    id='my-date-picker-end',
                    date=date(2024, 5, 24),
                    style={'margin-left': '10px', 'margin-top': '10px'}  
                ),
            ]),
        ], color="black"),  #colour of the date part 
        ], width=8),
    ],className='mb-2 mt-2'),
    dbc.Row([                                             # Row 2 with 5 col
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                           dbc.CardHeader(Lottie(options=options, style={'width': '60px', 'height': '60px'}, url=url_total)),
                           dbc.CardBody([
                                 html.H6('Survey'),
                                 html.H2(id='content-total', children="000")
                           ], style={'textAlign': 'center'})
                           ])
            ]),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                          dbc.CardHeader(Lottie(options=options, style={'width': '60px', 'height': '60px'}, url=url_trauma)),
                           dbc.CardBody([
                                 html.H6('Trauma'),
                                 html.H2(id='content-trauma', children="000")
                           ], style={'textAlign': 'center'})
                         
                ])
            ]),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                          dbc.CardHeader(Lottie(options=options, style={'width': '60px', 'height': '60px'}, url=url_male)),
                           dbc.CardBody([
                                 html.H6('Male'),
                                 html.H2(id='content-Male', children="000")
                           ], style={'textAlign': 'center'})
                ])
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                           dbc.CardHeader(Lottie(options=options, style={'width': '60px', 'height': '60px'}, url=url_female)),
                           dbc.CardBody([
                                 html.H6('Female'),
                                 html.H2(id='content-Female', children="000")
                           ], style={'textAlign': 'center'})
                ])
            ]),
        ], width=2),
    ],className='mb-2'),
    dbc.Row([                                     #Row 3 col 2
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='treemap', figure={}),  #treemap
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
                    dcc.Graph(id='doughnut-graph', figure={}),     # doughnut-graph
                ])
            ]),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='funnel-chart', figure={}),       # funnel-chart
                ])
            ]),
        ], width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='wordcloud', figure={}),   # wordcloud
                ])
            ]),
        ], width=3),
    ],className='mb-2'),
], fluid=True)

@app.callback(                                         #counts 
    Output('content-total', 'children'),
    Output('content-trauma', 'children'),
    Output('content-Male', 'children'),  
    Output('content-Female', 'children'),
    Input('my-date-picker-start', 'date'),
    Input('my-date-picker-end', 'date'),
)
def update_small_cards(start_date, end_date):
    dff_c = df_cnt.copy()
    dff_c['date'] = pd.to_datetime(dff_c['date'], format="%d-%m-%Y %H:%M", errors='coerce')
    dff_c = dff_c[(dff_c['date'] >= start_date) & (dff_c['date'] <= end_date)]
    total_count = len(dff_c)
    trauma_count = len(dff_c[(dff_c['trauma'].notna()) & (dff_c['trauma'] == 'YES')])
    male_count = len(dff_c[(dff_c['gender'].notna()) & (dff_c['gender'] == 'Male')])
    female_count = len(dff_c[(dff_c['gender'].notna()) & (dff_c['gender'] == 'Female')])

    return total_count, trauma_count, male_count, female_count


@app.callback(                                #wordcloud
    Output('wordcloud', 'figure'),
    Input('my-date-picker-start', 'date'),
    Input('my-date-picker-end', 'date'),
)
def update_wordcloud(start_date, end_date):
    dff = df_cnt.copy()
    dff = dff[(dff['date'] >= start_date) & (dff['date'] <= end_date)]
    
  

    positions = dff['words'].astype(str)

    my_wordcloud = WordCloud(
        background_color='white',
        height=275
    ).generate_from_text(' '.join(positions))

    fig_wordcloud = px.imshow(my_wordcloud, template='ggplot2',
                              title="Word Cloud of Emotions")
    fig_wordcloud.update_layout(margin=dict(l=20, r=20, t=30, b=20))
    fig_wordcloud.update_xaxes(visible=False)
    fig_wordcloud.update_yaxes(visible=False)

    return fig_wordcloud


@app.callback(                 #barchart
    Output('bar-chart', 'figure'),
    Input('my-date-picker-start', 'date'),
    Input('my-date-picker-end', 'date'),
)
def count_words(start_date, end_date):
    dff_c = df_cnt.copy()
    dff_c = dff_c[(dff_c['date'] >= start_date) & (dff_c['date'] <= end_date)]
    words_column = dff_c['words']

    word_count = {}
    for row in words_column:
        if isinstance(row, str):
            words = row.split(',')
            for word in words:
                word = word.strip()  # Remove leading/trailing whitespaces
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    words, counts = zip(*sorted_word_count[:10])  # Unzip the word-count pairs
    fig = go.Figure([go.Bar(x=words, y=counts)])
    fig.update_layout(title="Top 10 Emotions", xaxis_title="Words", yaxis_title="Count")
    return fig

@app.callback(                 # TreeMap
    Output('treemap', 'figure'),
    Input('my-date-picker-start', 'date'),
    Input('my-date-picker-end', 'date'),
)
def create_treemap(start_date, end_date):
    dff_c = df_cnt.copy()
    dff_c = dff_c[(dff_c['date'] >= start_date) & (dff_c['date'] <= end_date)]
    dff_c = dff_c[dff_c['trauma'] == 'YES']  # Filter rows where trauma is "yes"
    trauma_by_age = dff_c.groupby('age').size().reset_index(name='count')  # Group by age and count occurrences
    fig = px.treemap(trauma_by_age, path=['age'], values='count', title='Count of Trauma by Age')
    return fig


@app.callback(                 # Doughnut graph
    Output('doughnut-graph', 'figure'),
    Input('my-date-picker-start', 'date'),
    Input('my-date-picker-end', 'date'),
)
def create_doughnut_graph(start_date, end_date):
    dff_c = df_cnt.copy()
    dff_c = dff_c[(dff_c['date'] >= start_date) & (dff_c['date'] <= end_date)]
    aai_counts = dff_c['ai'].value_counts()
    fig = px.pie(names=aai_counts.index, values=aai_counts.values, hole=0.5, title='AI assistance ')
    return fig

@app.callback(                 # Funnel chart
    Output('funnel-chart', 'figure'),
    Input('my-date-picker-start', 'date'),
    Input('my-date-picker-end', 'date'),
)
def create_funnel_graph(start_date, end_date):
    dff_c = df_cnt.copy()
    dff_c = dff_c[(dff_c['date'] >= start_date) & (dff_c['date'] <= end_date)]
    dff_c = dff_c[(dff_c['support'] == 'No') & (dff_c['companion'] == 'Yes')]
    funnel_data = dff_c.groupby('age').size().reset_index(name='count')
    funnel_data = funnel_data.sort_values(by='count', ascending=False)
    fig = go.Figure(go.Funnel(y=funnel_data['age'], x=funnel_data['count'], textinfo="value+percent previous"))
    fig.update_layout(title="Funnel Chart by Age Group")
    return fig



if __name__=='__main__':
    app.run_server(debug=False, port=8001)