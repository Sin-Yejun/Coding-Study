import math
import copy
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        answer_arr = copy.deepcopy(img)
        rx = [0,0,0,-1,1,1,-1,1,-1]
        ry = [0,-1,1,0,0,1,1,-1,-1]
        m, n = len(img), len(img[0])
        for i in range(m):
            for j in range(n):
                S = 0
                cnt = 0
                for k in range(9):
                    mx = i + rx[k]
                    my = j + ry[k]
                    if 0 <= mx < m and 0<= my < n:
                        S += img[mx][my]
                        cnt += 1
                print(cnt)
                answer_arr[i][j] = math.floor(S/cnt)
        return answer_arr