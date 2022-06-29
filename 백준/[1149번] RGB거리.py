import sys
input = sys.stdin.readline
n = int(input())

arr = [list(map(int,input().split())) for i in range(n)]
arr = sum(arr,[])
for i in range(3, len(arr)):
    if i%3 == 2:
        arr[i] += min(arr[i-5], arr[i-4])
    elif i%3 == 1:
        arr[i] += min(arr[i-4], arr[i-2])
    else:
        arr[i] += min(arr[i-1], arr[i-2])
print(min(arr[-3:]))
