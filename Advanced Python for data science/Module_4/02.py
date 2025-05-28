'''
Interactive Plots with Plotly
Plotly is great for interactive visualizations.
'''
import pandas as pd

# Sample dataset
df = pd.DataFrame({
    'category': ['A', 'A', 'B', 'B', 'C'],
    'subcategory': ['X', 'Y', 'X', 'Y', 'X'],
    'value': [10, 20, 15, 25, 30]})


import plotly.express as px

fig = px.scatter(df, x='category', y='value', color='subcategory', title='Scatter Plot')
fig.show()