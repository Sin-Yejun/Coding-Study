import sys
input = sys.stdin.readline

n = int(input())
s = []
idx = 1
arr = []
for _ in range(n):
    x = int(input())
    if x > idx:
        s.append(idx)
        idx += 1
        arr.append('+')
        while s[-1] != x:
            s.append(idx)
            arr.append('+')
            idx += 1
        s.pop()
        arr.append('-')
    elif x < idx:
        if s[-1] == x:
            s.pop()
            arr.append('-')
    else:
        idx += 1
        arr.append('+')
        arr.append('-')


if arr.count('+') == arr.count('-') == n:
    [print(i) for i in arr]
else:
    print('NO')
