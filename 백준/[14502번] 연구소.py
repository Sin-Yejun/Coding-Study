import sys, copy

input = sys.stdin.readline

def bfs():
    test_map = copy.deepcopy(arr)
    q = set()
    for i in range(n):
        for j in range(m):
            if test_map[i][j] == 2:
                q.add((i,j))
    while q:
        x, y = q.pop()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < n and 0 <= my < m:
                if test_map[mx][my] == 0:
                    q.add((mx, my))
                    test_map[mx][my] = 2
    global result
    count = 0
    for i in range(n):
        for j in range(m):
            if test_map[i][j] == 0:
                count += 1
    result = max(result, count)
def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                make_wall(count+1)
                arr[i][j] = 0

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
result = 0
make_wall(0)
print(result)


