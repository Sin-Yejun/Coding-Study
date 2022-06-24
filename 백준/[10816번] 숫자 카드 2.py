import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
m = int(input())
sang = list(map(int,input().split()))

d = defaultdict(int)

for i in arr:
    d[i] += 1

for i in sang:
    print(d[i], end = ' ')
