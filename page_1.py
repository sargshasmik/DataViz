import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load data
df = pd.read_csv("HR_Employee_Attrition.csv")

# Layout for page 1
layout = html.Div([
    html.H1("HR Analytics Dashboard - Overview", style={'color': 'orange'}),
    dcc.Link('Go to Details', href='/page-2'),
    dcc.Graph(id='department-pie'),
    dcc.Graph(id='working-years-box')
])

# Define callbacks to update plots for page 1
def register_callbacks(app):
    @app.callback(
        Output('department-pie', 'figure'),
        Output('working-years-box', 'figure'),
        [Input('url', 'pathname')]
    )
    def update_page_1(pathname):
        if pathname == '/':
            # Calculate department distribution
            department_counts = df['Department'].value_counts()
            department_pie = px.pie(names=department_counts.index, values=department_counts.values, title='Distribution of Departments')

            # Create box plot for the distribution of working years by department using Plotly
            working_years_boxplot = px.box(df, x='Department', y='TotalWorkingYears', color='Department',
                                          title='Working Years Distribution by Department')

            # Update layout to add labels and adjust title
            working_years_boxplot.update_xaxes(title='Department')
            working_years_boxplot.update_yaxes(title='Working Years')
            working_years_boxplot.update_layout(title='Working Years Distribution by Department')

            return department_pie, working_years_boxplot
        return {}, {}
