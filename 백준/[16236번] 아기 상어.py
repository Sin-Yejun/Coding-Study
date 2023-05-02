# https://resilient-923.tistory.com/357
import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y, size):
    distance = [[0]*n for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    temp = []
    while q:
        cur_x, cur_y = q.popleft()
        #print(i, j, s)
        for move in range(4):
            nx = cur_x + dx[move]
            ny = cur_y + dy[move]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                    if arr[nx][ny] <= size:
                        q.append((nx,ny))
                        visited[nx][ny] = 1
                        distance[nx][ny] = distance[cur_x][cur_y]+1
                        if arr[nx][ny] < size and arr[nx][ny] != 0:
                            temp.append((nx,ny,distance[nx][ny]))
    return sorted(temp, key = lambda x : (-x[2], -x[0], -x[1]))
    
        
                
        
            
        

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dx = [-1, 0 ,1, 0]
dy = [0, 1, 0 ,-1]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            x = i
            y = j
size = 2
cnt = 0
result = 0
while 1:
    shark = bfs(x, y, size)
    if len(shark) == 0:
        break
    nx, ny, dist = shark.pop()

    result += dist
    arr[x][y], arr[nx][ny] = 0, 0
    x, y = nx, ny
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
print(result)
