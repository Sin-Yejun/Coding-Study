import sys, math
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parnet(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
arr = [tuple(map(float, input().split())) for _ in range(n)]
graph = []

for i in range(n):
    for j in range(i+1, n):
        if i != j:
            distance = math.dist(arr[i], arr[j])
            graph.append((distance, i, j))

parent = [0] * (n+1) # 초기화
result = 0

# 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# 간선을 비용순으로 정렬
graph.sort()

for edge in graph:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parnet(parent,a,b)
        result += cost

print(result)
            