import sys
from collections import defaultdict
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]

d = defaultdict(int)
unique = 0
for i in range(k):
    if d[arr[i]] == 0:
        unique += 1
    d[arr[i]] += 1

max_unique = unique + (1 if d[c] == 0 else 0)

for i in range(1, n):
    remove = arr[i-1]
    d[remove] -= 1
    if d[remove] == 0:
        unique -= 1
    
    add = arr[(i+k-1) % n]
    if d[add] == 0:
        unique += 1
    d[add] += 1

    current = unique + (1 if d[c] == 0 else 0)
    max_unique = max(max_unique, current)
print(max_unique)



