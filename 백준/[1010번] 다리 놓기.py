import sys
import math
n = int(input())
for _ in range(n):
    a, b = map(int,sys.stdin.readline().split())
    print(math.factorial(b)//(math.factorial(b-a)*math.factorial(a)))
