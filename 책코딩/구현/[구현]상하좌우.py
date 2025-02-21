n = int(input())
plans = input().split()
x, y = 1, 1
mx = [0, 0, -1, 1]
my = [-1, 1, 0, 0]
move_types = ["L", "R","U", "D"]

for plan in plans:
    for i in range(4):
        if plan == move_types[i]:
            nx = x + mx[i]
            ny = y + my[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
print(x, y)