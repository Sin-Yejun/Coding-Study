# https://www.acmicpc.net/problem/24479
import sys
from collections import deque

n, m, r = map(int, sys.stdin.readline().rstrip().split())

nodes = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
nodes_cnt = [0 for _ in range(n+1)]
for _ in range(m):
    tail, head = map(int, sys.stdin.readline().rstrip().split())
    nodes[tail].append(head)
    nodes[head].append(tail)

for i in range(n+1):
    nodes[i].sort(reverse=True)
cnt = 1

stack = deque()
stack.append(r)

while stack:
    cur_node = stack.pop()
    visited[cur_node] = True
    if nodes_cnt[cur_node] == 0:
        nodes_cnt[cur_node] = cnt
        cnt += 1

    for next_node in nodes[cur_node]:
        if not visited[next_node]:
            stack.append(next_node)


for cnt in nodes_cnt[1:]:
    print(cnt)
