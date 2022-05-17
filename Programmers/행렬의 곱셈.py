import numpy as np
def solution(arr1, arr2):
    A = np.array(arr1)
    B = np.array(arr2)
    
    R = np.dot(A,B)
    return R.tolist()
    
