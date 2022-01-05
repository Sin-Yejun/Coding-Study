import math
n, k = map(int,input().split())
num = math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
count = 0
for i in str(num)[::-1]:
    if i == '0':
        count +=1
    else:
        break
print(count)
