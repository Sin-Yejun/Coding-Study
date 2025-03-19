from collections import deque
n, computers = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

visited = [0]*(n+1)
def bfs():
    while q:
        x = q.popleft()
        visited[x] = 1
        idx = 0
        for i in range(n):
            if computers[x-1][i] == 1 and visited[i+1] == 0:
                q.append(i+1)
cnt = 0
for i in range(1, n+1):
    if visited[i]:
        continue
    q = deque([i])
    bfs()
    cnt += 1
print(cnt)