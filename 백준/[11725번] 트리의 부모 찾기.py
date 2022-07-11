import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
parents = [0 for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def DFS(start):
    for i in graph[start]:
        if parents[i] == 0:
            parents[i] = start
            DFS(i)

DFS(1)
#print(graph)
for i in range(2, len(parents)):
    print(parents[i])
