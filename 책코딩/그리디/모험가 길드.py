n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0
cnt = 0
for i in arr:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0
print(result)