import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# Import the page layouts and callback registration functions
from page_1 import layout as page_1_layout
from page_2 import layout as page_2_layout

# Define the layout of the app with navigation
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Update the index layout based on URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-2':
        return page_2_layout
    else:
        return page_1_layout

if __name__ == '__main__':
    from page_1 import register_callbacks as register_callbacks_page_1
    from page_2 import register_callbacks as register_callbacks_page_2
    register_callbacks_page_1(app)
    register_callbacks_page_2(app)
    app.run_server(host='0.0.0.0',debug=True, port=8090)


