import numpy as np

def maxtrix_multi_vector(matrix, vector):
  return np.dot(matrix, vector)

matrix = np.array([[ -1 , 1 , 1] , [0 , -4 , 9]])
vector = np.array([0 , 2 , 1])
print(maxtrix_multi_vector(matrix, vector))