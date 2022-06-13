from collections import deque

def solution(n, wires):
    
    def BFS(node):
        if not visited[node]:
            return
        arr.append(node)
        cnt = 0
        while arr:
            x = arr.popleft()
            if visited[x]:
                visited[x] = False
                cnt += 1
                for c in graph[x]:
                    arr.append(c)
        return cnt
    
    Min = 101
    for k in range(n-1):
        visited = [False] + [True] * n
        graph = [[] for i in range(n+1)]
        for i in range(len(wires)):
            if i == k:
                continue
            x = wires[i][0]
            y = wires[i][1]
            graph[x].append(y)
            graph[y].append(x)
        arr = deque()
        ans = []
        for i in range(1, n+1):
            x = BFS(i)
            if x:
                ans.append(x)
        Min = min(Min, abs(ans[0]-ans[1]))
    return Min
