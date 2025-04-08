import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

water_q = deque()
water_visited = [[False]*c for _ in range(r)]
swan_q = deque()
swan_next_q = deque()
swan_visited = [[False]*c for _ in range(r)]

swan_pos = []

# 초기 셋업: 물, 백조 위치
for i in range(r):
    for j in range(c):
        if arr[i][j] != 'X':
            water_q.append((i, j))
            water_visited[i][j] = True
        if arr[i][j] == 'L':
            swan_pos.append((i, j))

# 백조 시작 위치
sx, sy = swan_pos[0]
ex, ey = swan_pos[1]
swan_q.append((sx, sy))
swan_visited[sx][sy] = True

day = 0

def move_swan():
    while swan_q:
        x, y = swan_q.popleft()
        if (x, y) == (ex, ey):
            return True
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < r and 0 <= ny < c and not swan_visited[nx][ny]:
                swan_visited[nx][ny] = True
                if arr[nx][ny] == '.' or arr[nx][ny] == 'L':
                    swan_q.append((nx, ny))
                else:
                    swan_next_q.append((nx, ny))
    return False

def melt():
    for _ in range(len(water_q)):
        x, y = water_q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < r and 0 <= ny < c:
                if not water_visited[nx][ny] and arr[nx][ny] == 'X':
                    arr[nx][ny] = '.'
                    water_visited[nx][ny] = True
                    water_q.append((nx, ny))

# 메인 루프
while True:
    if move_swan():
        print(day)
        break
    melt()
    swan_q = swan_next_q
    swan_next_q = deque()
    day += 1
