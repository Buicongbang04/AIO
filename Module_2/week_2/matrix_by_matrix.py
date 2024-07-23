import numpy as np

def matrix_multi_matrix(matrix1, matrix2):
  return np.dot(matrix1, matrix2)

matrix1 = np.array([[1 , 2] , [3 , 4]])
matrix1 = np.reshape(matrix1 ,( -1 ,4) , "F") [0]
matrix2 = np.array([[1 , 1 , 1 , 1] ,[2 , 2 , 2 , 2] , [3 , 3 , 3 , 3] , [4 , 4 , 4 , 4]])

print(matrix_multi_matrix(matrix1, matrix2))
print(matrix1@matrix2)