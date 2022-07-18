import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int,input().split())
arr = [list(map(int,input().rstrip())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,-0,1,-1]
def bfs(a,b):
    cnt = 1
    q = deque()
    q.append((a,b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1:
                q.append((nx, ny))
                arr[nx][ny] = arr[x][y] + 1
    return arr[n-1][m-1]
print(bfs(0,0))
    
