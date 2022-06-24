import sys
input = sys.stdin.readline
m, n = map(int,input().split())
arr = list(map(int,input().split()))

sum = 0
sum_arr = [0]
for i in arr:
    sum += i
    sum_arr.append(sum)

for i in range(n):
    x, y = map(int,input().split())
    print(sum_arr[y] - sum_arr[x-1])
