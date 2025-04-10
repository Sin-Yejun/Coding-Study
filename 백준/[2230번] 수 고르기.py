import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

left, right = 0, 0
answer = float('inf')

while left < n and right < n:
    if arr[right] - arr[left] >= m:
        answer = min(answer, arr[right] - arr[left])
        left += 1
        # 만약 left가 right를 넘어가면 right를 left로 맞춰줌
        if left > right:
            right = left
    else:
        right += 1

print(answer)
