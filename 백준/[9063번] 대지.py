n = int(input())
Max_x = -10000
Min_x = 10000
Max_y = -10000
Min_y = 10000

for _ in range(n):
    x, y = map(int, input().split())
    Max_x = max(Max_x, x)
    Min_x = min(Min_x, x)
    Max_y = max(Max_y, y)
    Min_y = min(Min_y, y)

if n == 1:
    print(0)
else:
    print((Max_x - Min_x)*(Max_y-Min_y))
