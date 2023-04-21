from collections import deque

def BFS(n,k):
    queue = deque([(n,0)]) # (현재위치, 걸린시간)을 큐에 추가
    visited = set([n])   # 방문한 위치 저장

    while queue:
        pos, time = queue.popleft()

        if pos == k:     # 수빈이가 동생을 찾으면 시간 return
            return time

        # 걷거나 순간이동하여 다음 위치를 계산하고,
        # 방문한적 없는 위치면 큐에 추가
        next_pos = [pos-1, pos+1, pos*2]
        for p in next_pos:
            if 0 <= p <= 100000 and p not in visited:
                queue.append((p, time +1))
                visited.add(p)


n, k = map(int, input().split())

print(BFS(n,k))

