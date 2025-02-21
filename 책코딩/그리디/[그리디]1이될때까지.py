N, M = map(int, input().split())
ans = 0
while True:
    target = (N//M)*M
    ans += (N-target)
    N = target
    if N < M:
        break
    ans += 1
    N //= M
ans += (N-1)
print(ans)
