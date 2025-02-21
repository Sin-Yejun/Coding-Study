x, y= map(str, input())
x = ord(x)-97
y = int(y)
y -= 1

moves = [(-2, 1), (2, 1), (-2, -1), (-2, 1), (2,1),(2,-1),(-2,1),(-2,-1)]
cnt = 0
for mv in moves:
        
    if 0 <= x + mv[0] < 8 and 0 <= y + mv[1] < 8:
        cnt += 1

print(cnt)