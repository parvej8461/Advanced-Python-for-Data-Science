'''
Data Visualization
Customizing Matplotlib
Create publication-quality plots.
'''

import pandas as pd

# Sample dataset
df = pd.DataFrame({
    'category': ['A', 'A', 'B', 'B', 'C'],
    'subcategory': ['X', 'Y', 'X', 'Y', 'X'],
    'value': [10, 20, 15, 25, 30]})


import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.plot(df['value'], label='Values', color='blue', linewidth=2)
plt.title('Data Trend', fontsize=14)
plt.xlabel('Index', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.legend()
plt.grid(True)
plt.show()