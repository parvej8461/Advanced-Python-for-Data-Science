'''
Vectorized Operations with NumPy
NumPy enables fast, vectorized operations on arrays, crucial for numerical data science tasks.

Example: Matrix operations
'''
import numpy as np

# Create two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix multiplication
result = np.dot(A, B)
print(result)

# Element-wise operations
squared = np.square(A)
print(squared)