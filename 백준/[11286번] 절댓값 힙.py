import sys
import heapq
input = sys.stdin.readline
n = int(input())
h = []
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(h, (abs(x),x))
    else:
        if not h:
            print(0)
        else:
            print(heapq.heappop(h)[1])
