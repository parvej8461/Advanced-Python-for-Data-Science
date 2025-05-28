'''
Advanced Pandas Techniques
Pandas is the backbone of data manipulation in data science. Advanced techniques include efficient grouping, merging, and reshaping.

Example: Multi-level grouping and pivot tables
'''

import pandas as pd

# Sample dataset
df = pd.DataFrame({
    'category': ['A', 'A', 'B', 'B', 'C'],
    'subcategory': ['X', 'Y', 'X', 'Y', 'X'],
    'value': [10, 20, 15, 25, 30]
})

# Group by multiple columns and aggregate
grouped = df.groupby(['category', 'subcategory'])['value'].mean().unstack()
print(grouped)

# Pivot table with multiple aggregations
pivot = df.pivot_table(values='value', index='category', columns='subcategory', aggfunc=['mean', 'sum'])
print(pivot)
