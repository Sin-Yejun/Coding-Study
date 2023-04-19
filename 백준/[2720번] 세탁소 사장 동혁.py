T = int(input())
for _ in range(T):
    C = int(input())
    q = d = n = p = 0;
    if C // 25 > 0:
        q = C // 25
        C = C - 25*q
    if C // 10 > 0:
        d = C // 10
        C = C - 10*d
    if C // 5 > 0:
        n = C // 5
        C = C - 5*n
    p = C
    print(q, d, n, p)
