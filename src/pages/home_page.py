from dash import html
import dash_bootstrap_components as dbc

layout = html.Div([
    dbc.Container([
        dbc.Card([
            dbc.CardBody([

                html.H1("Telco Churn Predictor", className="page-title"),
                html.P(
                    "Welcome to the Telco Churn Predictor Dashboard — a powerful tool built to explore telecom customer churn behavior, evaluate machine learning models, and interactively predict churn risk.",
                    className="lead"
                ),

                html.Hr(),

                dbc.Row([
                    dbc.Col([
                        html.H4("Analytics", className="section-title"),
                        html.P("Explore customer trends, churn buckets, and feature correlations.")
                    ]),
                    dbc.Col([
                        html.H4("Info", className="section-title"),
                        html.P("Understand the dataset, the business context, and our project pipeline.")
                    ])
                ], className="mb-4"),

                dbc.Row([
                    dbc.Col([
                        html.H4("Performance", className="section-title"),
                        html.P("View model metrics, ROC curves, and select the best predictor.")
                    ]),
                    dbc.Col([
                        html.H4("Predict", className="section-title"),
                        html.P("Test our deployed model with real inputs and see the churn likelihood.")
                    ])
                ])
            ])
        ], className="hero-panel"),

        html.Div([
            html.H3("Meet the Team", className="team-header"),

            dbc.Row([
                dbc.Col(dbc.Card([
                    dbc.CardHeader("Glory Binkatabana", className="card-header-custom"),
                    dbc.CardBody([
                        html.P("Data Lead – Research, data sourcing, improvement recommendations.")
                    ])
                ], className="team-card"), md=3),

                dbc.Col(dbc.Card([
                    dbc.CardHeader("Storm Tarran", className="card-header-custom"),
                    dbc.CardBody([
                        html.P("EDA & Feature Engineering – Deep-dive into patterns & pre-processing.")
                    ])
                ], className="team-card"), md=3),

                dbc.Col(dbc.Card([
                    dbc.CardHeader("Tiaan Wessels", className="card-header-custom"),
                    dbc.CardBody([
                        html.P("Modeling & Evaluation – Trained ML models, compared results.")
                    ])
                ], className="team-card"), md=3),

                dbc.Col(dbc.Card([
                    dbc.CardHeader("Calvin Ronin Nijenhuis", className="card-header-custom"),
                    dbc.CardBody([
                        html.P("Deployment & App – Dash app builder, API integration, full deployment.")
                    ])
                ], className="team-card"), md=3)
            ])
        ], className="mt-5"),

        html.Footer("Powered by Render — Cloud Application Platform", className="footer-note mt-4")
    ], fluid=True, className="home-content")
])
