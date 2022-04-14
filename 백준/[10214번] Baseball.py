n = int(input())
for k in range(n):
    A = 0
    B = 0
    for _ in range(9):
        a, b = map(int,input().split())
        A += a
        B += b
    if A > B:
        print('Yonsei')
    elif A < B:
        print('Korea')
    else:
        print('Draw')

