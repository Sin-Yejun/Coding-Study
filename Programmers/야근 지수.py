import heapq
def solution(n, works):
    h = [-i for i in works]
    heapq.heapify(h)
    
    for _ in range(n):
        max_val = heapq.heappop(h)
        if max_val >= 0:
            break
        heapq.heappush(h, max_val + 1)
    return sum([k**2 for k in h])