import math
import numpy as np
import tensorly as tl
from tensorly.decomposition import parafac

N1 = N2 = N3 = 2

def myMatrixIndexSumFunc(i, j, k):
    return i + j + k + 3

T = np.fromfunction(myMatrixIndexSumFunc, [N1,N2,N3])
test2 = parafac(T, 2)

print(test2.weights)
print(test2.factors)
