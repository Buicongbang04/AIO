import numpy as np

def compute_dot_product(v1, v2):
  dot_product = np.dot(v1, v2)
  return dot_product

vector1 = np.array([1, 2, 3, 4, 5])
vector2 = np.array([5, 4, 3, 2, 1])
print(compute_dot_product(vector1, vector2))
