import dash
from dash import dcc, html, Input, Output, State, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
from io import StringIO
from dash.exceptions import PreventUpdate
import base64
import os

# load default dataset or else fallback to a sample
try:
    csv_path = os.path.join(os.path.dirname(__file__), '../../data/WA_Fn-UseC_-Telco-Customer-Churn.csv')
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    fallback_csv = StringIO("""customerID,gender,SeniorCitizen,Churn\n0001-FHJKL,Female,0,Yes\n0002-FHJKM,Male,0,No\n0003-FHJKN,Female,1,No""")
    df_default = pd.read_csv(fallback_csv)

layout = dbc.Container([
    html.H2("Dataset Preview", className="section-title mt-4"),

    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ', html.A('Select a CSV File')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin-bottom': '20px'
        },
        multiple=False
    ),

    html.Div(id='data-preview'),
    html.Hr(),
    html.H2("Statistical Summary", className="section-title"),
    html.Div(id='data-summary'),

    html.P("Note: This summary helps understand trends and data distributions used in the modeling process.", className="text-muted mt-3")
], fluid=False)


def parse_contents(contents):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        df = pd.read_csv(StringIO(decoded.decode('utf-8')))
        return df
    except Exception as e:
        return None

@dash.callback(
    Output('data-preview', 'children'),
    Output('data-summary', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename')
)
def update_output(contents, filename):
    if contents is None:
        df = df_default
    else:
        import base64
        df = parse_contents(contents)
        if df is None:
            raise PreventUpdate

    preview_table = dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.head(10).to_dict('records'),
        style_table={'overflowX': 'auto'},
        style_cell={
            'textAlign': 'left',
            'padding': '5px',
            'font-family': 'Segoe UI',
        },
        style_header={
            'backgroundColor': '#343a40',
            'color': 'white',
            'fontWeight': 'bold'
        },
    )

    summary_df = df.describe().reset_index()
    summary_table = dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in summary_df.columns],
        data=summary_df.to_dict('records'),
        style_table={'overflowX': 'auto'},
        style_cell={
            'textAlign': 'left',
            'padding': '5px',
            'font-family': 'Segoe UI',
        },
        style_header={
            'backgroundColor': '#343a40',
            'color': 'white',
            'fontWeight': 'bold'
        },
    )

    return preview_table, summary_table
