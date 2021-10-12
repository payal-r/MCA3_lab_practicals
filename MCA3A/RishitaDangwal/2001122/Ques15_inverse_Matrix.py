import numpy as np

matrix = np.array([
    [1, 2], [3, 4]
])

result = np.linalg.inv(matrix)
print(result)