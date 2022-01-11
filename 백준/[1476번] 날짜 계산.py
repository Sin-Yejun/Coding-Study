E, S, M = map(int,input().split())

e = 1
s = 1
m = 1
cnt = 1
while True:
    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1
    if E==e and S==s and M==m:
        print(cnt)
        break
    e += 1
    s += 1
    m += 1
    cnt += 1
