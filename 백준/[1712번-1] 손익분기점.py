a, b, c = map(int, input().split())
ans = 0
if c-b <= 0:
    print(-1)
else:
    ans = a//(c-b)+1
    print(ans)
