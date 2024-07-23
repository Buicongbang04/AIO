import numpy as np

def matrix_multi_matrix(matrix1, matrix2):
  return np.dot(matrix1, matrix2)

matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[2, 4, 6], [1, 3, 5], [7, 8, 9]])

print(matrix_multi_matrix(matrix1, matrix2))