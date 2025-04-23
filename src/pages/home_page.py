from dash import html
import dash_bootstrap_components as dbc

layout = html.Div([
    html.H1("Telco Churn Predictor", className="page-title"),

    html.P(
        "Welcome to the Telco Churn Predictor Dashboard. This app helps analyze churn patterns, evaluate models, and predict customer churn using real-world telecom data.",
        className="lead"
    ),

    html.Hr(),

    dbc.Row([
        dbc.Col([
            html.H4("Analytics", className="section-title"),
            html.P("Explore churn trends, feature relationships, and summary statistics.")
        ]),
        dbc.Col([
            html.H4("Info", className="section-title"),
            html.P("Get background on the dataset, preprocessing methods, and project rationale.")
        ])
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([
            html.H4("Performance", className="section-title"),
            html.P("View evaluation results, ROC curves, and model comparison metrics.")
        ]),
        dbc.Col([
            html.H4("Predict", className="section-title"),
            html.P("Test the model with custom inputs to predict customer churn likelihood.")
        ])
    ]),

    html.Hr(),

    html.H3("Meet the Team", className="team-header"),

    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardHeader("Glory Binkatabana", className="card-header-custom"),
            dbc.CardBody([
                html.P("Data Lead (Research relevant datasets, Continuous improvement, Reflection and future work)")
            ])
        ], className="team-card"), md=3),

        dbc.Col(dbc.Card([
            dbc.CardHeader("Tiaan Wessels", className="card-header-custom"),
            dbc.CardBody([
                html.P("EDA and Feature Engineer (Data Exploration and Pre-Processing)")
            ])
        ], className="team-card"), md=3),

        dbc.Col(dbc.Card([
            dbc.CardHeader("Storm Tarran", className="card-header-custom"),
            dbc.CardBody([
                html.P("Modeling and Evaluation (Develop ML Models)")
            ])
        ], className="team-card"), md=3),

        dbc.Col(dbc.Card([
            dbc.CardHeader("Calvin Ronin Nijenhuis", className="card-header-custom"),
            dbc.CardBody([
                html.P("Deployment and Presentation (Build web app, Implement model deployment, Testing, Documentation")
            ])
        ], className="team-card"), md=3),
    ], className="mb-5"),

    html.Footer("Powered by Render — Cloud Application Platform", className="footer-note")
], className="home-content")
