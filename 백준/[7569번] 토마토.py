import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
arr = []
q = deque()
for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))
        for k in range(m):
            if temp[j][k] == 1:
                q.append([i, j, k])
    arr.append(temp)

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

while q:
    x, y, z = q.popleft()

    for i in range(6):
        a = x + dx[i]
        b = y + dy[i]
        c = z + dz[i]
        if 0<=a<h and 0<=b<n and 0<=c<m and arr[a][b][c] == 0:
            q.append([a,b,c])
            arr[a][b][c] = arr[x][y][z]+1

day = 0
for i in arr:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day, max(j))
print(day-1)


                        
                        
                    
    
