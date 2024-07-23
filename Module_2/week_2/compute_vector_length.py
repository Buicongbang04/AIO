import numpy as np

def compute_vector_length(v):
  len_of_vector = np.sqrt(np.sum(v**2))
  return len_of_vector

vector = np.array([1, 2, 3, 4, 5])
print(compute_vector_length(vector))