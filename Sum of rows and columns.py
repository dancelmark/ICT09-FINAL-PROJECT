import numpy as np

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

sum_rows = np.sum(matrix, axis=1)
sum_columns = np.sum(matrix, axis=0)

print("Sum of rows:", sum_rows)
print("Sum of columns:", sum_columns)