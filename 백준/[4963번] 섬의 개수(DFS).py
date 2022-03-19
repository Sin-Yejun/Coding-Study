# https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%80%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%84%AC%EC%9D%98-%EA%B0%9C%EC%88%98-DFS-BFS
import sys
sys.setrecursionlimit(10000)
# 시계 방향
dX = [1, 1, 0, -1, -1, -1, 0, 1]
dY = [0, 1, 1, 1, 0, -1, -1, -1]

while True:
    def DFS(x, y, mapList, visitedList):
        visitedList[y][x] = True  # 방문 완료

        for i in range(8):
            nX = x + dX[i]
            nY = y + dY[i]

            if 0 <= nX < w and 0 <= nY < h:
                if visitedList[nY][nX] == False and mapList[nY][nX] == 1:
                    DFS(nX, nY, mapList, visitedList)

    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    mapList = []
    for i in range(h):
        mapList.append(list(map(int, input().split())))
    visitedList = [[False]*w for _ in range(h)]

    count = 0

    for i in range(h):
        for j in range(w):
            if visitedList[i][j] == False and mapList[i][j] == 1:
                DFS(j, i, mapList, visitedList)
                count += 1

    print(count)
