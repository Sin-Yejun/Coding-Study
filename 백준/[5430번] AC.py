from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    cmd = input().strip()
    l = int(input())
    arr = input().strip()
    arr = arr[1:len(arr)-1]
    if arr:
        arr = list(map(int,arr.split(',')))
    else:
        arr = []
    q = deque(arr)
    flag = 0
    reverse = 0
    for c in cmd:
        if c == 'R':
            reverse += 1
        elif c == 'D':
            if not q:
                print('error')
                flag = 1
                break
            elif reverse %2 == 1:
                q.pop()
            elif reverse %2 == 0:
                q.popleft()
    if flag == 0:
        if reverse % 2 == 1:
            q.reverse()
        print('['+','.join(map(str,list(q)))+']')
    

