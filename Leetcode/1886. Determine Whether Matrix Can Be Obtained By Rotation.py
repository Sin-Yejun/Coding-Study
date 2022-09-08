import numpy as np
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        MAT = np.array(mat)
        M90 = np.rot90(MAT,1)
        M180 = np.rot90(MAT,2)
        M270 = np.rot90(MAT,3)
        TAR = np.array(target)
        if np.array_equal(TAR,MAT):
            return True
        if np.array_equal(TAR,M90):
            return True
        if np.array_equal(TAR,M180):
            return True
        if np.array_equal(TAR, M270):
            return True
        return False
