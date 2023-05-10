import sys
from collections import deque
input = sys.stdin.readline
def bfs():
    q = deque()
    q.append((0, 0, 0)) # 시작점 (0, 0)에서 출발, 벽을 부수지 않았으므로 0
    visited[0][0][0] = 1 # 시작점 방문 체크
    while q:
        x, y, w = q.popleft()
        if x == n-1 and y == m-1: # 도착점에 도달하면
            return visited[x][y][w] # 최단 거리 반환
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 0 and visited[nx][ny][w] == 0: # 이동 가능하고 아직 방문하지 않은 경우
                    visited[nx][ny][w] = visited[x][y][w] + 1 # 거리 갱신 후 큐에 추가
                    q.append((nx, ny, w))
                elif board[nx][ny] == 1 and w == 0: # 벽이 있고, 벽을 아직 부수지 않은 경우
                    visited[nx][ny][1] = visited[x][y][w] + 1 # 벽을 부수고 이동한 거리 갱신 후 큐에 추가
                    q.append((nx, ny, 1))
    return -1 # 도착점에 도달하지 못한 경우 -1 반환

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)] # 3차원 visited 배열 초기화
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우 이동

print(bfs())
