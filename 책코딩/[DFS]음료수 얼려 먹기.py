import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 증가

n, m = map(int, input().split())
mat = [list(map(int, input())) for _ in range(n)]
print(mat)
def dfs(x, y):
    # ⚠️ 범위를 벗어났는지 먼저 체크
    if x < 0 or x >= n or y < 0 or y >= m:
        return False  # 인덱스 에러 방지
    
    if mat[x][y] == 0:
        mat[x][y] = 1  # 방문 처리
        # 네 방향 탐색
        dfs(x-1, y)  # 상
        dfs(x+1, y)  # 하
        dfs(x, y-1)  # 좌
        dfs(x, y+1)  # 우
        return True
    
    return False

ans = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):  # 새로운 덩어리 발견
            ans += 1

print(ans)
