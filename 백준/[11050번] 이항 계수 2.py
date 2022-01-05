import math
n, k = map(int,input().split())
print((math.factorial(n)//(math.factorial(k)*math.factorial(n-k)))%10007)
