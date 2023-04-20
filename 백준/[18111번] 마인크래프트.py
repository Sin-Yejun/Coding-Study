import sys
N, M, B = map(int, input().split())
arr = []
for _ in range(N):
    arr.extend(list(map(int, input().split())))
Min_time = sys.maxsize
block = 0
sig = 0

for i in range(min(arr), max(arr)+1):
    time = 0
    sig = 0
    tempB = B
    for j in range(len(arr)):
        if arr[j] == i:
            continue
        if arr[j] > i:  # 1번작업 (블럭제거)
            time += (arr[j]-i)*2
            tempB += arr[j]-i
        else:           # 2번작업 (블럭놓기)
            time += i-arr[j]
            tempB -= i-arr[j]
    if 0 <= tempB <= 6.4*10**7:
        if Min_time >= time:
            Min_time = time
            block = i


print(Min_time, block)
