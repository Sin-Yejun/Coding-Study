import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

start, end = map(int, input().split())

def dijkstra_max_weight(start, end):
    max_weight = [0] * (n + 1)
    max_weight[start] = float('inf')

    heap = [(-max_weight[start], start)]  # 최대힙: 큰 중량 우선

    while heap:
        weight, now = heapq.heappop(heap)
        weight = -weight

        if now == end:
            return weight

        for next_node, edge_weight in graph[now]:
            min_weight = min(weight, edge_weight)
            if min_weight > max_weight[next_node]:
                max_weight[next_node] = min_weight
                heapq.heappush(heap, (-min_weight, next_node))

    return 0

print(dijkstra_max_weight(start, end))
