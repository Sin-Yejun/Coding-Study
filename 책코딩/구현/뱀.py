from collections import deque
mx = [-1, 0, 1, 0]
my = [0, 1, 0, -1]
n = int(input())
k = int(input())
board = [[0]*(n+1) for _ in range(n+1)]
cmd = []
for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1 # 사과 표시
L = int(input())
cmd = dict()
for _ in range(L):
    x, c = input().split()
    x = int(x)
    if x not in cmd:
        cmd[x] = c
snakes = deque([1,1])
#print(cmd)
q = deque([(1,1, "E")])
def direction(x, y, pv_dir, c):
    current = "D"
    if pv_dir == "N":
        if c == "D":
            current = "E"
        else:
            current = "W"
    elif pv_dir == "S":
        if c == "D":
            current = "W"
        else:
            current = "E"
    elif pv_dir == "W":
        if c == "D":
            current = "N"
        else:
            current = "S"
    elif pv_dir == "E":
        if c == "D":
            current = "S"
        else:
            current = "N"
    return current
def moving(x, y, c):
    if c == "N":
        x -= 1
    elif c == "S":
        x += 1
    elif c == "W":
        y -= 1
    else:
        y += 1
    return [x, y]
time = 0
snake_len = 1
moving_history = deque([1,1])

while q:
    time += 1
    x, y, c= q.popleft()
    x, y = moving(x, y, c)
    
    # 벽닿으면 죽음
    if x < 1 or x > n or y < 1 or y > n: 
        break
    
    # 사과 먹으면
    if board[x][y] == 1: 
        snake_len += 1
        board[x][y] = 0
    else:   # 사과 없으면 꼬리 삭제  
        moving_history.popleft()

    if [x,y] in moving_history: # 몸 닿으면 죽음
        break

    while len(moving_history) > snake_len: # 꼬리 삭제
        moving_history.popleft()

    if time in cmd.keys():  # 방향 전환
        c = direction(x, y, c, cmd[time])

    q.append([x, y, c])
    moving_history.append([x, y])

print(time)