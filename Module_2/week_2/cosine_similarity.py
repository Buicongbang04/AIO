import numpy as np

def cosine_similarity(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError('vector1 and vector2 must have the same length')

    n = vector1.shape[0]

    tu = sum(np.array([float(vector1[i] + vector2[i]) for i in range(n)]))
    mau = sum(np.sqrt([vector1[i] ** 2 for i in range(n)])) * sum(np.sqrt([vector2[i] ** 2 for i in range(n)]))
    coss = tu / mau
    return coss


vector1 = np.array([1, 2, 3, 4])
vector2 = np.array([1, 0, 3, 0])
print("Cosine similarity: ", cosine_similarity(vector1, vector2))
