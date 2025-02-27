from itertools import combinations
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

chicken = []
house = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))

def get_chicken(h, c):
    sum_chikens = []
    for i in range(len(h)):
        x, y = h[i]
        min_chicken = 1e9
        for j in range(len(c)):
            a, b = c[j]
            distance = abs(x - a) + abs(y - b)
            min_chicken = min(min_chicken, distance)
        sum_chikens.append(min_chicken)
    return sum_chikens

min_ans = 1e9
for k in combinations(chicken, m):
    ans = get_chicken(house, list(k))
    min_ans = min(min_ans, sum(ans))
print(min_ans)
