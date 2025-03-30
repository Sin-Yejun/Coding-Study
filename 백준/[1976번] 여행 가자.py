# 플루이드-위셜

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dest = list(map(int, input().split()))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
for i in range(n):
    graph[i][i] = 1
start = dest[0]-1
flag = True
for i in range(1, len(dest)):
    x = dest[i]-1
    if graph[start][x] == 0:
        flag = False
        break
    start = dest[i]-1

if flag:
    print("YES")
else:
    print("NO")

# 유니온-파인드
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    if rootA != rootB:
        parent[rootB] = rootA
    
n = int(input())
m = int(input())
parent = [i for i in range(n)]

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 1:
            union(i, j)
plan = list(map(int, input().split()))
root = find(plan[0]-1)

flag = True
for city in plan:
    if find(city-1) != root:
        print("NO")
        flag = False
        break
if flag:
    print("YES")

