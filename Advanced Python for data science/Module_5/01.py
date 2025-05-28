'''Concurrency for Data Science
Parallel Processing with multiprocessing
Speed up data preprocessing.
'''



from multiprocessing import Pool

def process_chunk(chunk):
    return chunk['value'].mean()

'''
This function processes each chunk independently
 by calculating the mean of the 'value' column.
   Each process will receive one chunk and return one result.

'''

chunks = [df[i:i+1000] for i in range(0, len(df), 1000)]
'''
This splits the DataFrame into chunks of 1000 rows each:

range(0, len(df), 1000) creates indices: 0, 1000, 2000, 3000...
Each chunk is a slice: df[0:1000], df[1000:2000], etc.
For a 5000-row DataFrame, you'd get 5 chunks
'''
with Pool(4) as pool:
    results = pool.map(process_chunk, chunks)
print(results)

'''
Pool(4): Creates 4 worker processes (using 4 CPU cores)
pool.map(): Distributes chunks across workers and collects results
Context manager (with): Automatically closes the pool when done
'''