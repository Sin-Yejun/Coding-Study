import sys
from collections import deque
input = sys.stdin.readline

r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
q = deque()
q = set([(0,0,arr[0][0])])
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
MAX_LEN = 0
while q:
    x, y, s = q.pop()
    MAX_LEN = max(MAX_LEN, len(s))
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < r and 0 <= my < c and arr[mx][my] not in s:
            q.add((mx, my, s+arr[mx][my]))
print(MAX_LEN)
