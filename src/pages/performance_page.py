from dash import html

layout = html.Div([
    html.H1("Model Performance", className="page-title"),
    html.P("This page shows evaluation metrics, ROC curves, and feature importance comparisons for the trained models.")
])
