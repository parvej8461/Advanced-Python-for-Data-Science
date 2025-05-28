'''
Memory-Efficient Data Handling
Use dtype optimization and chunking for large datasets.

Example: Reducing memory usage

'''
import pandas as pd
# Optimize dtypes
df = pd.DataFrame({'A': [1, 2, 3], 'B': [1.5, 2.5, 3.5]})
df['A'] = df['A'].astype('int8')  # Use smaller dtype
df['B'] = df['B'].astype('float32')

# Chunking for large CSV
for chunk in pd.read_csv('large_dataset.csv', chunksize=1000):
    print(chunk.shape)  # Process each chunk