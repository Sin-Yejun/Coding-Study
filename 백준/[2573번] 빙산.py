import sys
from collections import deque
input = sys.stdin.readline

n, m = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

ice_berg = []   # 현재 빙산 위치
next_ice_berg = []
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            ice_berg.append((i, j))

def melt():
    global next_ice_berg
    melts = []
    for x, y in ice_berg:
        count = 0
        for i in range(4):
            cx, cy = x + dx[i], y + dy[i]
            if 0 <= cx < n and 0 <= cy < m and arr[cx][cy] == 0:
                count += 1
        melts.append((x, y, count))
    for x, y, cnt in melts:
        arr[x][y] = max(0, arr[x][y] - cnt)
        if arr[x][y] > 0:
            next_ice_berg.append((x, y))

def check():
    total = len(ice_berg)
    count = 1
    q = deque([ice_berg[0]])
    visited = [[False]*m for _ in range(n)]
    visited[ice_berg[0][0]][ice_berg[0][1]] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < n and 0 <= cy < m:
                if arr[cx][cy] != 0 and not visited[cx][cy]:
                    visited[cx][cy] = True
                    count += 1
                    q.append((cx, cy))
    #print(total, count)
    if total == count:  # 빙하가 한덩이
        return True
    else:               # 빙하기 분리됨
        return False

def print_arr():
    print()
    for line in arr:
        print(' '.join(map(str, line)))
    print()

answer = 0
while True:
    if not ice_berg:
        answer = 0  # 전부 녹았으면 답은 0
        break
    if not check():  # 분리됨
        break
    melt()
    answer += 1
    ice_berg = next_ice_berg
    next_ice_berg = []
print(answer)