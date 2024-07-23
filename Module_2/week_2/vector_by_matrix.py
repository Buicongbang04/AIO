import numpy as np

def maxtrix_multi_vector(matrix, vector):
  return np.dot(matrix, vector)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vector = np.array([1, 2, 3])
print(maxtrix_multi_vector(matrix, vector))