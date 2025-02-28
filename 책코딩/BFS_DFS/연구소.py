from collections import deque
from itertools import combinations
import sys
import copy
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

virus = []
wall = []
possible_wall = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            virus.append((i, j))
        if arr[i][j] == 1:
            wall.append((i, j))
        if arr[i][j] == 0:
            possible_wall.append((i, j))
def bfs(arr):
    q = deque(virus)
    while q:
        x, y = q.popleft()
        arr[x][y] = 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0:
                    q.append((nx, ny))
    return sum(i.count(0) for i in arr)

Max = 0
for x in combinations(possible_wall, 3):
    new_arr = copy.deepcopy(arr)
    for i in x:
        wx, wy = i[0], i[1]
        new_arr[wx][wy] = 1
    Max = max(Max, bfs(new_arr))
print(Max)



