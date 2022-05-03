import heapq
def solution(scoville, K):
    heap_q = []
    for i in scoville:
        heapq.heappush(heap_q,i)
    cnt = 0
    while heap_q[0] < K:
        if len(heap_q) == 1:
            return -1
        a = heapq.heappop(heap_q)
        b = heapq.heappop(heap_q)
        heapq.heappush(heap_q,a+b*2)
        cnt += 1
    return cnt
