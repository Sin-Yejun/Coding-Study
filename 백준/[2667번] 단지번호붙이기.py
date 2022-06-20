from collections import deque
n = int(input())
arr = [list(map(int,input())) for i in range(n)]
visited = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def DFS(x,y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if arr[x][y] == 1:
        global count
        count += 1
        arr[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False

count = 0
result = 0
num = []
for i in range(n):
    for j in range(n):
        if DFS(i,j):
            num.append(count)
            count = 0
num.sort()
print(len(num))
for i in num:
    print(i)
