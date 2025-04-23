import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc

# import layouts from page files
from pages.home_page import layout as home_layout
from pages.analytics_page import layout as analytics_layout
from pages.info_page import layout as info_layout
from pages.performance_page import layout as performance_layout
from pages.predict_page import layout as predict_layout

# initialize app
app = dash.Dash(__name__, use_pages=False, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# navigation bar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dcc.Link("Home", href="/", className="nav-link")),
        dbc.NavItem(dcc.Link("Analytics", href="/analytics", className="nav-link")),
        dbc.NavItem(dcc.Link("Info", href="/info", className="nav-link")),
        dbc.NavItem(dcc.Link("Performance", href="/performance", className="nav-link")),
        dbc.NavItem(dcc.Link("Predict", href="/predict", className="nav-link")),
    ],
    brand="Telco Churn Predictor",
    brand_href="/",
    color="primary",
    dark=True,
    className="custom-navbar"
)

# app layout
app.layout = html.Div([
    dcc.Location(id='url'),
    navbar,
    html.Div(id='page-content', className='page-content')
])

# route different pages
@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/analytics":
        return analytics_layout
    elif pathname == "/info":
        return info_layout
    elif pathname == "/performance":
        return performance_layout
    elif pathname == "/predict":
        return predict_layout
    elif pathname == "/":
        return home_layout
    else:
        return html.Div([
            html.H2("404 - Page not found"),
            html.P("The page you are looking for does not exist.")
        ])

# run server
if __name__ == '__main__':
    app.run_server(debug=True, port=8050, host='0.0.0.0')
