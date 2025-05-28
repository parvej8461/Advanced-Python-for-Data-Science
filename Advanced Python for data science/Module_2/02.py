'''
Using functools and itertools
These modules streamline data processing pipelines.
'''
from functools import reduce
from itertools import groupby

import pandas as pd
# Sample dataset
df = pd.DataFrame({
    'category': ['A', 'A', 'B', 'B', 'C'],
    'subcategory': ['X', 'Y', 'X', 'Y', 'X'],
    'value': [10, 20, 15, 25, 30]})

# Reduce to compute product
values = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, values)
print(product)  # Output: 24

'''
reduce applies a function cumulatively to items in a sequence, reducing them to a single value:

It takes the first two elements (1, 2) and applies the lambda: 1 × 2 = 2
Then takes the result (2) and the next element (3): 2 × 3 = 6
Then takes the result (6) and the next element (4): 6 × 4 = 24

This is equivalent to: ((1 * 2) * 3) * 4 = 24
'''

# Groupby for sorted data
sorted_data = sorted(df['category'])
groups = {key: list(group) for key, group in groupby(sorted_data)}
print(groups)
'''

groupby groups consecutive identical elements together.
Important: The data must be sorted first
because groupby only groups consecutive items.
'''