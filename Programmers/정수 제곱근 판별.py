import math
def solution(n):
    temp = math.pow(n,0.5)
    if temp - int(temp) == 0:
        return (temp+1)**2
    else:
        return -1
