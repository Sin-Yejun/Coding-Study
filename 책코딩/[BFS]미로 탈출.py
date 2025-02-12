from collections import deque
n, m = map(int, input().split())
mat = [list(map(int, input())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(a, b):
    q = deque()
    q.append([a, b])


    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<=ny <m:
                if mat[nx][ny] == 1:
                    mat[nx][ny] = mat[x][y] + 1
                    q.append([nx, ny])
    return mat[n-1][m-1]
print(bfs(0,0))
