import sys
from collections import defaultdict
from itertools import combinations
input = sys.stdin.readline

def init_dict():
    for key, val in d.items():
        d[key] = 10000

def sum_distance(arr):
    init_dict()
    total = 0
    for x1, y1 in house:
        for x2, y2 in arr:
            if d[(x1, y1)] > abs(x1-x2)+abs(y1-y2):
                d[(x1, y1)] = abs(x1-x2)+abs(y1-y2)
    for key, val in d.items():
        total += val
    return total

d = defaultdict(int)
house = []
chicken = []
n, m = map(int, input().split())
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            house.append((i+1,j+1))
            d[(i+1, j+1)] = 10000
        elif line[j] == 2:
            chicken.append((i+1,j+1))
ans = 10000
for t in combinations(chicken, m):
    x = sum_distance(t)
    if ans > x:
        ans = x

print(ans)
