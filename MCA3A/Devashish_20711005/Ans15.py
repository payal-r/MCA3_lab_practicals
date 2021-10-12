import numpy as np

matrix = np.array([
    [4, 3], [2, 1]
])

result = np.linalg.inv(matrix)
print(result)