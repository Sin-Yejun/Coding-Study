# https://enhjh.tistory.com/56
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = -1000000

def go(px, py, index, sum):
    if index == k:
        global answer
    
        if answer < sum:
            answer = sum
        
        return

    for x in range(px, n):
        for y in range(py if x==px else 0, m):
            # 현재 위치 방문했었는지 확인
            if visited[x][y]:
                continue

            ok = True
            # 동서남북 방문 했었는지 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny]:
                        ok = False            
            # 방문
            if ok:
                visited[x][y] = True
                go(x, y, index+1, sum+arr[x][y])
                visited[x][y] = False


go(0, 0, 0, 0)

print(answer)
