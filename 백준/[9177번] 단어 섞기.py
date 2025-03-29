import sys
from collections import deque
input = sys.stdin.readline

def solve():
    n = int(input())
    for k in range(1, n + 1):
        s1, s2, s3 = input().split()
        visited = set()
        q = deque()
        q.append((0, 0))  # (index in s1, index in s2)
        success = False

        while q:
            i, j = q.popleft()
            if i + j == len(s3):
                success = True
                break
            if (i, j) in visited:
                continue
            visited.add((i, j))

            if i < len(s1) and s1[i] == s3[i + j]:
                q.append((i + 1, j))
            if j < len(s2) and s2[j] == s3[i + j]:
                q.append((i, j + 1))

        if success:
            print(f'Data set {k}: yes')
        else:
            print(f'Data set {k}: no')

solve()
