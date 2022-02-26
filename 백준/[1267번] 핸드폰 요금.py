import sys
inf = sys.stdin.readline

n = int(inf())
arr = list(map(int,inf().split()))

A = 0
B = 0

for i in arr:
    A += (i//30+1)*10
    B += (i//60+1)*15

if A == B:
    print('Y M',A)
elif A < B:
    print('Y',A)
else:
    print('M',B)
