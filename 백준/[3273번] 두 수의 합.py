import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
x = int(input())
arr.sort()
left = 0
right = n-1
answer = 0
while left < right:
    temp = arr[left] + arr[right]
    if temp == x:
        answer += 1
    if temp < x:
        left += 1
    else:
        right -= 1
print(answer)
