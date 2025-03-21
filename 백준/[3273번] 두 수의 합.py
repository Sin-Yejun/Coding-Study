import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
x = int(input())
arr.sort()

left, right = 0, len(arr)-1
cnt = 0
while left < right:
    total = arr[left]+arr[right]
    if total == x:
        cnt += 1
        left += 1
    elif total < x:
        left += 1
    else:
        right -= 1

print(cnt)