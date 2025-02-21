N, M = map(int, input().split())
ans = 0
for _ in range(N):
    data = list(map(int, input().split()))
    min_val = min(data)
    ans = max(ans, min_val)

print(ans)

