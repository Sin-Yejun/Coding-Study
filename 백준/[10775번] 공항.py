import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
def union(x):
    root = find(x)
    if root == 0:
        return False
    parent[root] = find(root - 1)  # 도킹 처리 → 아래 게이트로 연결
    return True

G = int(input())
P = int(input())
parent = [i for i in range(G+1)]
cnt = 0
for _ in range(P):
    x = int(input())  # 도킹하려는 게이트 번호
    if union(x):
        cnt += 1
    else:
        break  # 더 이상 도킹 불가능하면 종료

print(cnt)