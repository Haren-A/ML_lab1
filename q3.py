import numpy as np

def matrix_power(A, m):
    
    if len(A) != len(A[0]):
        return "Error: The matrix is not square."
    
  
    A = np.array(A)
    
    
    result = np.linalg.matrix_power(A, m)
    
    return result


A = [
    [1, 2],
    [3, 4]
]
m = 3

result = matrix_power(A, m)
print("A^{} =".format(m))
print(result)
