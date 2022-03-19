import sys
from collections import deque

n = int(input())
arr = list(map(int,input().split()))
start = int(input())
visited = [False]*n

def BFS(n):
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        visited[x-1] = True
        if 0 < x + arr[x-1] <= len(arr):
            q.append(x + arr[x-1])
        
        if 0 < x - arr[x-1] < len(arr):
            q.append(x - arr[x-1])
BFS(start)
print(visited.count(True))
