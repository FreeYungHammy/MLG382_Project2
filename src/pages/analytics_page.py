import dash_bootstrap_components as dbc
from dash import html

layout = dbc.Container([
    html.Div([
        html.H1("Analytics Overview", className="page-title text-center mb-4"),
        html.P(
            "Explore key patterns in the dataset through correlations, categorical group comparisons, and numeric feature distributions to understand churn behavior.",
            className="subtitle"
        ),

        html.Hr(),

        html.H2("Feature Correlation Analysis", className="section-title mt-4"),
        html.Img(src="corr_matrix_unannotated.png", className="img-fluid mb-3"),
        html.P(
            "This unannotated correlation heatmap provides a compact visual of feature relationships using color intensity. It complements the annotated version by highlighting broader patterns without numeric distraction."
        ),

        html.Img(src="corr_matrix_annotated.png", className="img-fluid mb-3"),
        html.P(
            "This annotated correlation matrix highlights relationships between numerical and encoded categorical features. Strong correlations like between LogTotalCharges and tenure can guide dimensionality."
        ),

        html.H2("Churn Distribution by Categorical Groups", className="section-title mt-5"),
        html.Img(src="churn_tenure_bucket.png", className="img-fluid mb-3"),
        html.P(
            "This chart shows that customers with lower tenure have a significantly higher churn rate. This insight can help with retention strategies targeting new users."
        ),

        html.Img(src="churn_contract_type.png", className="img-fluid mb-3"),
        html.P(
            "This comparison reveals that customers on one-year contracts churn far less than those on monthly agreements, underscoring the value of locking in longer-term plans."
        ),

        html.H2("Numeric Feature Impact on Churn", className="section-title mt-5"),
        html.Img(src="log_totalcharges_box.png", className="img-fluid mb-3"),
        html.P(
            "Lower total charges are correlated with higher churn, suggesting newer or lower-value customers are more at risk."
        ),

        html.Img(src="monthlycharges_box.png", className="img-fluid mb-3"),
        html.P(
            "Customers with higher monthly charges are also more likely to churn. These insights support revenue-driven segmentation strategies."
        ),

        html.Footer("Analytics powered by historical telecom data — processed for educational insights.", className="footer-note text-muted mt-5 mb-3 text-center")
    ],
    className="hero-panel"
)], fluid=False)
