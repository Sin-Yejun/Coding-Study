# https://hbj0209.tistory.com/143
N, S = map(int,input().split())
arr = list(map(int,input().split()))

left = 0
right = 0

s = arr[0]
ans = 100001

while True:
    if s >= S:
        s -= arr[left]
        ans = min(ans, right - left + 1)
        left += 1
    else:
        right += 1
        if right == N:
            break
        s += arr[right]

if ans == 100001:
    print(0)
else:
    print(ans)
