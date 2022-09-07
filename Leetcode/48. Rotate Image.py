import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #Reverse
        l, r = 0, len(matrix)-1
        
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            r -= 1
            l += 1
            
        #Transpose
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        
