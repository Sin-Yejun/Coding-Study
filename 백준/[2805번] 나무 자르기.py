#pypy3
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 1
end = max(arr)

while start <= end:
    mid = (start+end) // 2
    cnt = 0
    for i in arr:
        if i >= mid:
            cnt += i-mid
    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
