import sys
n = int(input())
arr = []
for _ in range(n):
    a = int(sys.stdin.readline())
    if a != 0:
        arr.append(a)
    else:
        del arr[-1]
print(sum(arr))
