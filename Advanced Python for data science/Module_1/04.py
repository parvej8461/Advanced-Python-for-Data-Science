'''
Dask for Large Datasets
Dask handles datasets larger than memory by parallelizing operations.

Example: given below
'''
import dask.dataframe as dd

# Load large dataset
ddf = dd.read_csv('large_dataset.csv')
# Compute mean in parallel
mean_value = ddf['column'].mean().compute()
print(mean_value)