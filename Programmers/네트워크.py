from collections import deque
def solution(n, computers):
    arr = [[] for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                arr[i+1].append(j+1)
    visited = [True] * (n+1)
    answer = []
    def BFS(node):
        if not visited[node]:
            return
        global idx
        q = deque()
        q.append(node)
        cnt = 0
        while q:
            num = q.popleft()
            if visited[num]:
                cnt += 1
            visited[num] = False
            for i in arr[num]:
                if visited[i] == True:
                    q.append(i)
        answer.append(idx)
    if not sum(arr,[]):
        return n
    global idx
    idx = 0
    for i in range(1,n+1):
        BFS(i)
        idx += 1
    return len(answer)
    
        
