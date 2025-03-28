from collections import deque, defaultdict

n, k = map(int, input().split())

q = deque([n])
d = defaultdict(int)
visited = [False]*100001
visited[n] = True

while q:
    x = q.popleft()

    if x == k:
        path = []
        t = x
        while t != n:
            path.append(t)
            t = d[t]
        path.append(n)
        print(len(path) - 1)  # 이동 횟수
        print(*reversed(path))  # 경로 출력
        break

    for temp in (x - 1, x + 1, x * 2):
        if 0 <= temp <= 100000 and not visited[temp]:
            visited[temp] = True
            d[temp] = x
            q.append(temp)