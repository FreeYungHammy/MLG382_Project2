import dash_bootstrap_components as dbc
from dash import html

layout = dbc.Container([
    html.Div([
        html.H1("Analytics Dashboard", className="page-title text-center mb-4"),

        html.P("This section provides visual insights into customer churn trends, feature correlations, and numeric influences. Each visualization has been selected for its ability to justify modeling decisions and business interpretation."),

        html.Hr(),

        # 1: Feature Relationships
        html.H3("Feature Correlation Analysis", className="section-title mt-4"),
        html.Img(src="/assets/Annotated Correlation Matrix of Selected Features.png", style={"width": "100%", "marginBottom": "20px"}),
        html.P("This annotated correlation matrix highlights relationships between numerical and encoded categorical features. Strong correlations like between LogTotalCharges and tenure can guide dimensionality."),

        # 2: Churn by Group
        html.H3("Churn Distribution by Categorical Groups", className="section-title mt-4"),
        html.Img(src="/assets/Churn Rate by Tenure Bucket.png", style={"width": "100%", "marginBottom": "20px"}),
        html.P("This chart shows that customers with lower tenure have a significantly higher churn rate. This insight can help with retention strategies targeting new users."),

        html.Img(src="/assets/Churn Rate One Year vs Monthly.png", style={"width": "100%", "marginBottom": "20px"}),
        html.P("This comparison reveals that customers on one-year contracts churn far less than those on monthly agreements, underscoring the value of locking in longer-term plans."),

        # 3: Numerical Feature Impact
        html.H3("Numeric Feature Impact on Churn", className="section-title mt-4"),
        html.Img(src="/assets/LogTotalCharges by Churn.png", style={"width": "100%", "marginBottom": "20px"}),
        html.P("Lower total charges are correlated with higher churn, suggesting newer or lower-value customers are more at risk."),

        html.Img(src="/assets/Monthly Charges vs Churn.png", style={"width": "100%", "marginBottom": "20px"}),
        html.P("Customers with higher monthly charges are also more likely to churn. These insights support revenue-driven segmentation strategies."),

        html.Footer("Data visualizations based on engineered features from the Telco churn dataset.", className="footer-note text-muted mt-5 mb-3 text-center")
    ], className="hero-panel")
], fluid=False)
