import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from afinn import Afinn

# Initialize Dash app
app = dash.Dash(__name__)

# Load AFINN lexicon
afinn = Afinn()

# Define app layout
app.layout = html.Div([
    html.H1('Amazon Sentiment Analysis App', style={'color': 'navy'}),
    html.Div([
        html.P('Enter your Amazon product review below:', style={'margin-bottom': '5px'}),
        dcc.Textarea(
            id='input-text',
            placeholder='Type here...',
            style={'width': '100%', 'height': 200},
            value=''  # Provide a default value to ensure the component exists
        ),
        html.Button('Analyze', id='analyze-btn', style={'margin-top': '10px'}),
    ], style={'margin-bottom': '20px'}),
    html.Div(id='output', style={'font-size': '18px', 'font-weight': 'bold'})
])

# Define callback to handle analysis button click
@app.callback(
    Output('output', 'children'),
    [Input('analyze-btn', 'n_clicks')],
    [dash.dependencies.State('input-text', 'value')]
)
def analyze_sentiment(n_clicks, user_input):
    if n_clicks is None:
        return ''
    
    if not user_input:
        return html.Div('Please enter a product review.', style={'color': 'red'})
    
    # Calculate sentiment score using AFINN
    sentiment_score = afinn.score(user_input)
    
    # Determine sentiment category
    if sentiment_score > 0:
        sentiment_category = 'Positive'
        color = 'green'
    elif sentiment_score < 0:
        sentiment_category = 'Negative'
        color = 'red'
    else:
        sentiment_category = 'Neutral'
        color = 'blue'
    
    # Display sentiment score and category
    return html.Div([
        html.Div(f'Sentiment Score: {sentiment_score}', style={'color': color}),
        html.Div(f'Sentiment Category: {sentiment_category}', style={'color': color})
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
