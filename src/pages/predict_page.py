import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State
import pandas as pd
import numpy as np
import joblib
import os
from dash.exceptions import PreventUpdate

# Load the model
model_path = os.path.join(os.path.dirname(__file__), '../../artifacts/model_1.pkl')
try:
    model = joblib.load(model_path)
except Exception as e:
    model = None
    print("Model loading failed:", e)

# Example feature inputs for the deployed model
input_features = [
    'LogTotalCharges', 'MonthlyCharges_scaled',
    'Contract_One year', 'Contract_Two year',
    'PaperlessBilling_Yes', 'PaymentMethod_Electronic check',
    'tenure_4–12', 'tenure_13–24', 'tenure_25–48', 'tenure_49+'
]

def create_prediction_layout():
    return dbc.Container([
        html.Div([
            html.H1("Churn Prediction", className="page-title text-center mb-4"),
            html.P("Use the form below to simulate a customer profile and see the churn prediction result.", className="subtitle"),

            html.Hr(),

            dbc.Row([
                dbc.Col([
                    dbc.Label("Log Total Charges"),
                    dbc.Input(id='input-totalcharges', type='number', placeholder="e.g., 6.5"),

                    dbc.Label("Monthly Charges (scaled)", className="mt-3"),
                    dbc.Input(id='input-monthlycharges', type='number', placeholder="e.g., 0.4"),

                    dbc.Label("Contract Type"),
                    dcc.Dropdown(id='input-contract', options=[
                        {'label': 'Month-to-Month', 'value': 'month'},
                        {'label': 'One year', 'value': '1yr'},
                        {'label': 'Two year', 'value': '2yr'}
                    ], value='month')
                ], md=6),

                dbc.Col([
                    dbc.Label("Paperless Billing"),
                    dcc.Dropdown(id='input-paperless', options=[
                        {'label': 'Yes', 'value': 'yes'},
                        {'label': 'No', 'value': 'no'}
                    ], value='yes'),

                    dbc.Label("Payment Method"),
                    dcc.Dropdown(id='input-payment', options=[
                        {'label': 'Electronic Check', 'value': 'electronic'},
                        {'label': 'Other', 'value': 'other'}
                    ], value='electronic'),

                    dbc.Label("Tenure Bucket"),
                    dcc.Dropdown(id='input-tenure', options=[
                        {'label': '4–12', 'value': 'tenure_4–12'},
                        {'label': '13–24', 'value': 'tenure_13–24'},
                        {'label': '25–48', 'value': 'tenure_25–48'},
                        {'label': '49+', 'value': 'tenure_49+'},
                    ], value='tenure_4–12')
                ], md=6)
            ], className="mb-4"),

            dbc.Button("Predict", id='predict-btn', color="primary", className="mt-2 mb-4"),
            html.Div(id='prediction-output', className="text-center")

        ], className="hero-panel")
    ], fluid=False)

layout = create_prediction_layout()
import dash_bootstrap_components as dbc
from dash import html, dcc

layout = dbc.Container([
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
                    className='form-control',
                    placeholder='Select contract type'
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
                    className='form-control',
                    placeholder='Select billing type'
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
                    className='form-control',
                    placeholder='Select payment method'
                )
            ], md=4),

            dbc.Col([
                dbc.Label("Tenure Group"),
                dcc.Dropdown(
                    id='input-tenure',
                    options=[
                        {'label': 'Tenure_0-12', 'value': 'Tenure_0-12'},
                        {'label': 'Tenure_12-24', 'value': 'Tenure_12-24'},
                        {'label': 'Tenure_24-48', 'value': 'Tenure_24-48'},
                        {'label': 'Tenure_48-60', 'value': 'Tenure_48-60'},
                        {'label': 'Tenure_gt_60', 'value': 'Tenure_gt_60'}
                    ],
                    className='form-control',
                    placeholder='Select tenure bucket'
                )
            ], md=4),
        ], className="mb-4"),

        dbc.Button("Predict Churn", id='predict-btn', color='primary', className='mb-3'),

        html.Div(id='prediction-output')

    ], className="hero-panel")
], fluid=False)
