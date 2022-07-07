# https://hongcoding.tistory.com/93
import sys
import heapq
input = sys.stdin.readline
n = int(input())
left_h = []
right_h = []
for _ in range(n):
    x = int(input())
    if len(left_h) == len(right_h):
        heapq.heappush(left_h,-x)
    else:
        heapq.heappush(right_h,x)

    if right_h and right_h[0] < -left_h[0]:
        left_val = heapq.heappop(left_h)
        right_val = heapq.heappop(right_h)

        heapq.heappush(left_h, - right_val)
        heapq.heappush(right_h, -left_val)
    print(-left_h[0])
        
