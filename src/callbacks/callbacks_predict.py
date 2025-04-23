import pandas as pd
from dash import Input, Output, State, callback
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import pickle
import os

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), '../../artifacts/model_1.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Feature columns expected by the model
input_features = [
    'LogTotalCharges', 'MonthlyCharges_scaled',
    'Contract_One year', 'Contract_Two year',
    'PaperlessBilling_Yes', 'PaymentMethod_Electronic check',
    'Tenure_0-12', 'Tenure_12-24', 'Tenure_24-48',
    'Tenure_48-60', 'Tenure_gt_60'
]
def register_callbacks(app):
    @app.callback(
        Output('prediction-output', 'children'),
        Input('predict-btn', 'n_clicks'),
        State('input-totalcharges', 'value'),
        State('input-monthlycharges', 'value'),
        State('input-contract', 'value'),
        State('input-paperless', 'value'),
        State('input-payment', 'value'),
        State('input-tenure', 'value')
    )
    def make_prediction(n_clicks, totalcharges, monthlycharges, contract, paperless, payment, tenure):
        if not n_clicks:
            raise PreventUpdate

        if totalcharges is None or monthlycharges is None or contract is None or paperless is None or payment is None or tenure is None:
            return dbc.Alert("Please fill in all fields to predict churn.", color="danger")

        input_vector = pd.DataFrame([[0]*len(input_features)], columns=input_features)

        input_vector['LogTotalCharges'] = totalcharges
        input_vector['MonthlyCharges_scaled'] = monthlycharges
        input_vector['Contract_One year'] = 1 if contract == '1yr' else 0
        input_vector['Contract_Two year'] = 1 if contract == '2yr' else 0
        input_vector['PaperlessBilling_Yes'] = 1 if paperless == 'yes' else 0
        input_vector['PaymentMethod_Electronic check'] = 1 if payment == 'electronic' else 0

        if tenure in input_vector.columns:
            input_vector[tenure] = 1

        try:
            pred_proba = model.predict_proba(input_vector)[0][1]
            pred_label = model.predict(input_vector)[0]
        except Exception as e:
            return dbc.Alert(f"Prediction error: {e}", color="warning")

        return dbc.Alert(
            f"Predicted Churn Probability: {pred_proba:.2%} — Prediction: {'Churn' if pred_label == 1 else 'No Churn'}",
            color="danger" if pred_label == 1 else "success"
        )
