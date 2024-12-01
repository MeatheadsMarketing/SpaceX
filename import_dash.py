import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Create Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    html.H1("SpaceX Launch Records Dashboard", 
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    # Dropdown menu for launch sites
    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'ALL'},
            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
            {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
            {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}
        ],
        value='ALL',
        placeholder='Select a Launch Site here',
        searchable=True
    ),
    
    # Placeholder Div for additional dynamic content
    html.Div(id='output-container')
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)