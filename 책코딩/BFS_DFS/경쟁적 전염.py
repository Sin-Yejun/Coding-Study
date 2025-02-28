from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
virus = []
for i in range(n):
    for j in range(n):
        if arr[i][j] > 0:
            virus.append((i, j, arr[i][j], 1))
virus = sorted(virus, key= lambda x:x[2])
q = deque(virus)
while q:
    x, y, c, t = q.popleft()
    if t > S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y]
                q.append((nx, ny, arr[x][y], t+1))
            else:
                continue
print(arr[X-1][Y-1])