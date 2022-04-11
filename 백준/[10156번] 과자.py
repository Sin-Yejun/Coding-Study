a, b, c = map(int,input().split())

buy = a*b

if buy <= c:
    print(0)
else:
    print(buy-c)
