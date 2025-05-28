# Functional Programming for Data Science
'''
Lambda Functions and map/filter
Functional programming simplifies data transformations.

'''
# example
import pandas as pd
# Sample dataset
df = pd.DataFrame({
    'category': ['A', 'A', 'B', 'B', 'C'],
    'subcategory': ['X', 'Y', 'X', 'Y', 'X'],
    'value': [10, 20, 15, 25, 30]})
# Apply a transformation to a pandas column
df['value_squared'] = df['value'].map(lambda x: x ** 2)

# Filter rows
filtered = df[df['value'].apply(lambda x: x > 15)]
print(filtered)
