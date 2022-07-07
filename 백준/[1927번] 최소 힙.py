import sys
import heapq
input = sys.stdin.readline
h = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x == 0:
        if not h:
            print(0)
        else:
            print(abs(heapq.heappop(h)))
    else:
        heapq.heappush(h,x)
