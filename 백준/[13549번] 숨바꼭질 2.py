from collections import deque

def BFS():
    queue = deque([(n,0)]) # (현재위치, 걸린시간)을 큐에 추가
       # 방문한 위치 저장
    result = [0]
    visited[n][0] = 0
    visited[n][1] = 1
    while queue:
        pos, time = queue.popleft()
        #print(pos, time)
        if pos == k:     # 수빈이가 동생을 찾으면 시간 return
            return
        # 걷거나 순간이동하여 다음 위치를 계산하고,
        # 방문한적 없는 위치면 큐에 추가
        move = [pos-1, pos+1, pos*2]
        for p in move:
            if 0 <= p <= 100000:
                if visited[p][0] == -1:
                    visited[p][0] = visited[pos][0]+1
                    visited[p][1] = visited[pos][1]
                    queue.append((p, time+1))
                elif visited[p][0] == visited[pos][0]+1:
                    visited[p][1] += visited[pos][1]

n, k = map(int, input().split())
visited = [[-1,0] for _ in range(1000001)]
BFS()
print(visited[k][0])
print(visited[k][1])
