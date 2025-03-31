x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# 벡터 AB, AP 계산
ABx, ABy = x2 - x1, y2 - y1
APx, APy = x3 - x1, y3 - y1

# 외적
cross = ABx * APy - ABy * APx

# 판별
if cross > 0:   # 반시계 방향
    print(1)
elif cross < 0: # 시계 방향
    print(-1)
else:           # 직선 위
    print(0)