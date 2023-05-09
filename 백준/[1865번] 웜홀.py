import sys
input = sys.stdin.readline


def bellman_ford():
    dist = [0] * (n+1)  # 시작 정점에서 각 정점까지의 최단 거리를 저장하는 배열

    # 최단 거리 갱신을 n-1번 반복
    for _ in range(1, n):
        for u in range(1, n+1):
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    # 음의 사이클 검사
    has_negative_cycle = False
    for u in range(1, n+1):
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                has_negative_cycle = True
                break
        if has_negative_cycle:
            break

    return has_negative_cycle

T = int(input())
for _ in range(T):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e,t))
        graph[e].append((s,t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s].append((e, -t))
    if bellman_ford():
        print('YES')
    else:
        print('NO')
    
