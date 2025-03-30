import sys
from collections import defaultdict
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root
        size[x_root] += size[y_root]
    return size[x_root]

T = int(input())
for _ in range(T):
    parent = dict()
    size = dict()
    n = int(input())
    id_map = dict()
    next_id = 0

    for _ in range(n):
        a, b = input().split()

        for name in (a, b):
            if name not in parent:
                parent[name] = name
                size[name] = 1
        print(union(a, b))