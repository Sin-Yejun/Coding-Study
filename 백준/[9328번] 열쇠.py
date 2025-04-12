import sys
from collections import deque, defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    arr = ['.'* (m+2)]
    for _ in range(n):
        arr.append('.'+input().strip()+'.')
    arr.append('.'*(m+2))
    key = set(input().strip())
    if '0' in key:
        key = set()

    n += 2
    m += 2

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    q = deque()
    q.append((0, 0))
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True
    count = 0
    door = defaultdict(list)
    while q:
        x, y = q.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if 0 <= cx < n and 0<= cy < m and not visited[cx][cy]:
                if arr[cx][cy] != '*':  # 벽이 아니라면
                    visited[cx][cy] = True
                    if arr[cx][cy] == '$':
                        count += 1

                    if arr[cx][cy].islower():
                        if arr[cx][cy] not in key:
                            key.add(arr[cx][cy])
                            if arr[cx][cy].upper() in door:
                                for i in door[arr[cx][cy].upper()]:
                                    q.append(i)

                    if arr[cx][cy].isupper():
                        if arr[cx][cy].lower() not in key:
                            door[arr[cx][cy]].append((cx, cy))
                            continue
                    q.append((cx, cy))

    print(count)