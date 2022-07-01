import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
for i in range(n):
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))
    arr = deque(arr)
    num = arr[k]
    arr[k] = 0
    cnt = 0
    while True:
        #print(arr)
        if max(arr) == arr[0] and max(arr) >= num:
            arr.popleft()
            cnt += 1
            if not arr:
                print(cnt)
                break
            continue
        elif max(arr) <= num and arr[0] == 0:
            print(cnt+1)
            break
        arr.rotate(-1)

            
        
    
