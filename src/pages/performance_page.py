import dash_bootstrap_components as dbc
from dash import html, dash_table
import pandas as pd

# Predefined model performance data
model_comparison = pd.DataFrame({
    'Model': ['Logistic Regression', 'Random Forest (tuned)'],
    'Accuracy': [0.7943, 0.7616],
    'Precision': [0.6543, 0.5627],
    'Recall': [0.4731, 0.4462],
    'ROC-AUC': [0.8314, 0.7919]
})

table_component = dash_table.DataTable(
    columns=[{"name": i, "id": i} for i in model_comparison.columns],
    data=model_comparison.to_dict('records'),
    style_table={'overflowX': 'auto'},
    style_cell={
        'textAlign': 'center',
        'padding': '10px',
        'font-family': 'Segoe UI',
    },
    style_header={
        'backgroundColor': '#343a40',
        'color': 'white',
        'fontWeight': 'bold'
    }
)

layout = dbc.Container([
    html.Div([
        html.H1("Model Performance Evaluation", className="page-title text-center mb-4"),
        html.P(
            "This section presents key performance indicators and visual comparisons between machine learning models used to predict customer churn.",
            className="subtitle"
        ),

        html.Hr(),

        html.H2("Model Comparison Table", className="section-title mt-4"),
        table_component,

        html.H2("ROC Curve Comparison", className="section-title mt-4"),
        html.Img(src="roc_curve_all_models.png", className="img-fluid mb-3"),
        html.P(
            "This ROC curve illustrates the true positive rate against the false positive rate for Logistic Regression and Random Forest models. The closer the curve follows the left-hand border and then the top border of the ROC space, the more accurate the model."
        ),

        html.H2("Calibration Curve (Logistic Regression)", className="section-title mt-5"),
        html.Img(src="calibration_curve.png", className="img-fluid mb-3"),
        html.P(
            "The calibration curve helps determine if the predicted probabilities are representative of actual outcomes. This plot shows that the Logistic Regression model produces probabilities that are reasonably calibrated against real churn events."
        ),

        html.Footer("Evaluation powered by ROC and probability calibration — aiding fair model comparison and trust in prediction reliability.", className="footer-note text-muted mt-5 mb-3 text-center")
    ],
    className="hero-panel")
], fluid=False)
