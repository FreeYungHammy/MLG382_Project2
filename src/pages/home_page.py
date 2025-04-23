import dash_bootstrap_components as dbc
from dash import html, dcc
import pandas as pd
import plotly.express as px
from io import StringIO
import os

try:
    csv_path = os.path.join(os.path.dirname(__file__), '../../data/WA_Fn-UseC_-Telco-Customer-Churn.csv')
    df_default = pd.read_csv(csv_path)
except FileNotFoundError:
    fallback_csv = StringIO("""customerID,gender,SeniorCitizen,Churn\n0001-FHJKL,Female,0,Yes\n0002-FHJKM,Male,0,No\n0003-FHJKN,Female,1,No""")
    df_default = pd.read_csv(fallback_csv)

churn_counts = df_default["Churn"].value_counts().reset_index()
churn_counts.columns = ['Churn', 'Count']

# plotting 
fig = px.bar(
    churn_counts,
    x='Churn',
    y='Count',
    color='Churn',
    title='Customer Churn Distribution',
    text='Count',
    color_discrete_sequence=["#00c7b1", "#ff6b6b"]
)

fig.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(color='#2c3e50'),
    title_x=0.5
)
fig.update_traces(textposition='auto')

# layout
layout = dbc.Container([
    html.Div([
        html.H1("Telco Churn Predictor", className="page-title text-center mb-4"),
        html.P(
            "Welcome to the Telco Churn Predictor Dashboard — a powerful tool built to explore telecom customer churn behavior, evaluate machine learning models, and interactively predict churn risk.",
            className="subtitle"
        ),

        html.Hr(),

        dbc.Row([
            dbc.Col([
                html.H4("Analytics", className="section-title"),
                html.P([
                    "Explore customer trends, churn buckets, and feature correlations. ",
                    html.A("Go to Analytics →", href="/analytics", className="link-style")
                ])
            ]),
            dbc.Col([
                html.H4("Info", className="section-title"),
                html.P([
                    "Understand the dataset, the business context, and our project pipeline. ",
                    html.A("Go to Info →", href="/info", className="link-style")
                ])
            ])
        ], className="mb-4"),

        dbc.Row([
            dbc.Col([
                html.H4("Performance", className="section-title"),
                html.P([
                    "View model metrics, ROC curves, and select the best predictor. ",
                    html.A("Go to Performance →", href="/performance", className="link-style")
                ])
            ]),
            dbc.Col([
                html.H4("Predict", className="section-title"),
                html.P([
                    "Test our deployed model with real inputs and see the churn likelihood. ",
                    html.A("Go to Predict →", href="/predict", className="link-style")
                ])
            ])
        ]),

        html.Hr(),

        html.H3("Churn Rate in the Dataset", className="section-title"),
        dbc.Row([
            dbc.Col([
                dcc.Graph(figure=fig)
            ])
        ], className="mb-5"),

        html.H3("Meet the Team", className="team-header"),
        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardHeader("Glory Binkatabana", className="card-header-custom"),
                dbc.CardBody([
                    html.P("Data Lead — Research, data sourcing, improvement recommendations.")
                ])
            ], className="team-card"), md=3),

            dbc.Col(dbc.Card([
                dbc.CardHeader("Storm Tarran", className="card-header-custom"),
                dbc.CardBody([
                    html.P("EDA & Feature Engineering — Deep-dive into patterns & pre-processing.")
                ])
            ], className="team-card"), md=3),

            dbc.Col(dbc.Card([
                dbc.CardHeader("Tiaan Wessels", className="card-header-custom"),
                dbc.CardBody([
                    html.P("Modeling & Evaluation — Trained ML models, compared results.")
                ])
            ], className="team-card"), md=3),

            dbc.Col(dbc.Card([
                dbc.CardHeader("Calvin Ronin Nijenhuis", className="card-header-custom"),
                dbc.CardBody([
                    html.P("Deployment & App — Dash app builder, API integration, full deployment.")
                ])
            ], className="team-card"), md=3),
        ], className="mb-5"),

        html.Footer("Powered by Render — Cloud Application Platform", className="footer-note text-muted mt-5 mb-3 text-center")
    ], className="hero-panel")
], fluid=False)
