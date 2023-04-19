import math
N, B = map(int, input().split())
arr = []
while N >= 1:
    if N % B < 10:
        arr.append(int(N%B))
    else:
        arr.append(chr(int(N%B)+55))
    N = N //B
print(''.join(map(str,arr[::-1])))
    
