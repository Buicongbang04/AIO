import numpy as np

def compute_vector_length(v):
  len_of_vector = np.sqrt(np.sum(v**2))
  return len_of_vector

vector = np.array([ -2 , 4 , 9 , 21])
print(compute_vector_length(vector))