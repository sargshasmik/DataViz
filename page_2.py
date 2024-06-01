import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load data
df = pd.read_csv("HR_Employee_Attrition.csv")

# Layout for page 2
layout = html.Div([
    html.H1("HR Analytics Dashboard - Details", style={'color': 'orange'}),
    dcc.Link('Go to Overview', href='/'),
    dcc.Graph(id='income-by-dep-hist'),
    dcc.Graph(id='job-role-bar'),
    dcc.Graph(id='educ-field-bar')
])

# Define callbacks to update plots for page 2
def register_callbacks(app):
    @app.callback(
        Output('income-by-dep-hist', 'figure'),
        Output('job-role-bar', 'figure'),
        Output('educ-field-bar', 'figure'),
        [Input('url', 'pathname')]
    )
    def update_page_2(pathname):
        if pathname == '/page-2':
            # Create histograms for monthly income by department using Plotly
            income_histograms = px.histogram(df, x='MonthlyIncome', color='Department', facet_col='Department',
                                            facet_col_wrap=4, barmode='overlay', title='Histograms of Monthly Income by Department')

            # Update layout to add labels and adjust title
            income_histograms.update_xaxes(title='Monthly Income')
            income_histograms.update_yaxes(title='Frequency')
            income_histograms.update_layout(title='Histograms of Monthly Income by Department')

            # Calculate the count of each job role
            jobrole_counts = df['JobRole'].value_counts()

            # Create horizontal bar plot for the count of each job role using Plotly
            jobrole_count_plot = px.bar(x=jobrole_counts.values, y=jobrole_counts.index, orientation='h',
                                        labels={'x': 'Count', 'y': 'Role'},
                                        title='Count of Each Role', color_discrete_sequence=px.colors.qualitative.Set2)

            educ_counts = df['EducationField'].value_counts()

            # Create horizontal bar plot for the count of each education field using Plotly
            educ_count_plot = px.bar(x=educ_counts.values, y=educ_counts.index, orientation='h',
                                        labels={'x': 'Count', 'y': 'Education Field'},
                                        title='Count of Education Field', color_discrete_sequence=px.colors.qualitative.D3)

            return income_histograms, jobrole_count_plot, educ_count_plot
        return {}, {}, {}
