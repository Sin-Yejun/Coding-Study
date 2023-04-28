import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(1)
    visited[1] = False
    while q:
        now = q.popleft()
        for move in range(1, 7):
            check_move = now+move
            if 0 < check_move <= 100 and visited[check_move]:
                if check_move in ladder.keys():
                    check_move = ladder[check_move]
                if check_move in snake.keys():
                    check_move = snake[check_move]
                if visited[check_move]:
                    q.append(check_move)
                    visited[check_move] = False
                    arr[check_move] = arr[now] + 1
                    
                


n, m = map(int, input().split())
ladder = dict()
snake = dict()

for _ in range(n):
    i, j = map(int, input().split())
    ladder[i] = j

for _ in range(m):
    i, j = map(int, input().split())
    snake[i] = j

arr = [0]*101
visited = [True]*101
bfs()
print(arr[100])

    

