import numpy as np
class Solution:
    def isHappy(self, n: int) -> bool:
        arr = list(map(int,str(n)))
        temp = []
        while True:
            val = np.dot(arr,arr)
            if val in temp:
                return False
            temp.append(val)
            if val == 1:
                return True
            arr = list(map(int,str(val)))
