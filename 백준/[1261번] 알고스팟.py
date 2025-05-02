import sys, heapq
input = sys.stdin.readline
m, n = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
dist = [[float('inf')]*(m) for _ in range(n)]
dist[0][0] = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

heap = []
heapq.heappush(heap, (0, 0, 0))

while heap:
    w, x, y = heapq.heappop(heap)
    if x == n-1 and y == m-1:
        print(w)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            cost = w + arr[nx][ny]
            #print(nx, ny)
            if dist[nx][ny] > cost:
                
                dist[nx][ny] = cost
                heapq.heappush(heap, (cost, nx, ny))
