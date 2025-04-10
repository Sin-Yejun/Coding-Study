import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0
total = 0
ans = 0
while True:
    if total >= m:
        if total == m:
            ans += 1
        total -= arr[left]
        left += 1
    elif right == n:
        break
    else:
        total += arr[right]
        right += 1

print(ans)