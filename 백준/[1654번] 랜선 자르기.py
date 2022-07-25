# https://jjini-3-coding.tistory.com/11
import sys
input = sys.stdin.readline
n, m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(n):
        cnt += arr[i] // mid
    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
