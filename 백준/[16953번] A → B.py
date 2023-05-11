from collections import deque


def bfs():
    q = deque([(A, 1)])
    visited.add(A)
    while q:
        x, c = q.popleft()
        if x == B:
            return c
        move = [x*10+1, x*2]
        for m in move:
            if 1 <= m <= 1e9 and m not in visited:
                q.append((m,c+1))
                visited.add(m)
    return -1

A, B = map(int, input().split())
visited = set()

print(bfs())
