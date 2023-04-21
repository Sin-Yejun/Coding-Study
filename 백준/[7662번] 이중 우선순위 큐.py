import heapq
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    max_heap = []
    min_heap = []
    keys = [0]*n
    for key in range(n):
        c, i = input().split()
        i = int(i)
       
        if c == 'I':
            heapq.heappush(min_heap, (i,key))
            heapq.heappush(max_heap, (-i,key))
            keys[key] = 1
        else:
            if i == 1:
                while max_heap and not keys[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    keys[heapq.heappop(max_heap)[1]] = 0
            else:
                while min_heap and not keys[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    keys[heapq.heappop(min_heap)[1]] = 0
    while max_heap and not keys[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not keys[min_heap[0][1]]:
        heapq.heappop(min_heap)
                    
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
    
