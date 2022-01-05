# https://mococoding.tistory.com/14
import math
n = int(input())
num = math.factorial(n)
arr = list(map(int,str(num)))
cnt = 0
for x in arr[::-1]:
    if x != 0:
        break
    cnt+=1
print(cnt)
