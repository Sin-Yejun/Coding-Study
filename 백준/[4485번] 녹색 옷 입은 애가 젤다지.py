import sys, heapq
from collections import deque
input = sys.stdin.readline

count = 1
while True:
    n = int(input())    
    if n == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(n)]
    dist = [[float('inf')]*n for _ in range(n)]
    dist[0][0] = arr[0][0]
    heap = []
    heapq.heappush(heap, (arr[0][0], 0, 0))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while heap:
        w, x, y = heapq.heappop(heap)
        if x==n-1 and y == n-1:
            print(f"Problem {count}: {w}")
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = w + arr[nx][ny]
                if dist[nx][ny] > cost:
                    dist[nx][ny] = cost
                    heapq.heappush(heap, (cost, nx, ny))
    count += 1
