from collections import deque
import copy

'''
1. 진입차수가 0인 노드를 큐에 넣는다.
2. 큐가 빌 때까지 다음의 과정을 반복한다.
    I. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
    II. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
'''
v = int(input())
indegree = [0]*(v+1)
graph = [[] for _ in range(v+1)]
times = [0] * (v+1)
for i in range(1, v+1):
    inputs = list(map(int, input().split()))
    times[i] = inputs[0]
    for x in inputs[1:-1]:
        indegree[i] += 1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(times)
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now]+times[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, v+1):
        print(result[i])

topology_sort()


        