import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 재귀 깊이 설정 (큰 트리 대응)

# 입력
n, root, q = map(int, input().split())  # 정점 개수
connect = [[] for _ in range(n + 1)]  # 인접 리스트

for _ in range(n - 1):
    u, v = map(int, input().split())
    connect[u].append(v)
    connect[v].append(u)

# 트리 구성
parent = [0] * (n + 1)
children = [[] for _ in range(n + 1)]
size = [0] * (n + 1)  # 서브트리 정점 수

def makeTree(current, par):
    parent[current] = par
    for node in connect[current]:
        if node != par:
            children[current].append(node)
            makeTree(node, current)

def countSubtreeNodes(current):
    size[current] = 1  # 자기 자신 포함
    for node in children[current]:
        countSubtreeNodes(node)
        size[current] += size[node]

makeTree(root, -1)
countSubtreeNodes(root)

# 질의 처리 예시
for _ in range(q):
    u = int(input())
    print(size[u])
