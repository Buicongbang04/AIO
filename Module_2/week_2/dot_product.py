import numpy as np

def compute_dot_product(v1, v2):
  dot_product = np.dot(v1, v2)
  return dot_product

vector1 = np.array([0 , 1 , -1 , 2])
vector2 = np.array([2 , 5 , 1 , 0])
print(compute_dot_product(vector1, vector2))
