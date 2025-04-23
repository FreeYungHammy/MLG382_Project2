import dash_bootstrap_components as dbc
from dash import html, dcc

# Wrapped in a function for clean modularity
def create_prediction_layout():
    return dbc.Container([
        html.Div([
            html.H1("Customer Churn Prediction", className="page-title text-center mb-4"),
            html.P(
                "Use this form to enter customer information and predict the likelihood of churn.",
                className="subtitle"
            ),

            html.Hr(),

            dbc.Row([
                dbc.Col([
                    dbc.Label("Log of Total Charges"),
                    dcc.Input(id='input-totalcharges', type='number', className='form-control', placeholder='e.g. 8.9')
                ], md=4),

                dbc.Col([
                    dbc.Label("Monthly Charges (scaled)"),
                    dcc.Input(id='input-monthlycharges', type='number', className='form-control', placeholder='e.g. 0.45')
                ], md=4),

                dbc.Col([
                    dbc.Label("Contract Type"),
                    dcc.Dropdown(
                        id='input-contract',
                        options=[
                            {'label': 'Month-to-month', 'value': 'monthly'},
                            {'label': 'One year', 'value': '1yr'},
                            {'label': 'Two year', 'value': '2yr'}
                        ],
                        placeholder='Select contract type',
                        className='form-control'
                    )
                ], md=4),
            ], className="mb-3"),

            dbc.Row([
                dbc.Col([
                    dbc.Label("Paperless Billing"),
                    dcc.Dropdown(
                        id='input-paperless',
                        options=[
                            {'label': 'Yes', 'value': 'yes'},
                            {'label': 'No', 'value': 'no'}
                        ],
                        placeholder='Select billing type',
                        className='form-control'
                    )
                ], md=4),

                dbc.Col([
                    dbc.Label("Payment Method"),
                    dcc.Dropdown(
                        id='input-payment',
                        options=[
                            {'label': 'Electronic Check', 'value': 'electronic'},
                            {'label': 'Other', 'value': 'other'}
                        ],
                        placeholder='Select payment method',
                        className='form-control'
                    )
                ], md=4),

                dbc.Col([
                    dbc.Label("Tenure Group"),
                    dcc.Dropdown(
                        id='input-tenure',
                        options=[
                            {'label': '4-12 months', 'value': 'tenure_4–12'},
                            {'label': '13-24 months', 'value': 'tenure_13–24'},
                            {'label': '25-48 months', 'value': 'tenure_25–48'},
                            {'label': '49+ months', 'value': 'tenure_49+'},
                        ],
                        placeholder='Select tenure bucket',
                        className='form-control'
                    )
                ], md=4),
            ], className="mb-4"),

            dbc.Button("Predict Churn", id='predict-btn', color='primary', className='mb-3'),

            html.Div(id='prediction-output')

        ], className="hero-panel")
    ], fluid=False)

# Export layout for use in app
layout = create_prediction_layout()
