# https://claude-u.tistory.com/433
def DFS(x, y, number):
    if len(number) == 6:
        if number not in result:
            result.append(number)
        return

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        ddx = x + dx[i]
        ddy = y+ dy[i]
        if 0 <= ddx < 5 and 0 <= ddy < 5:
            DFS(ddx, ddy, number + matrix[ddx][ddy])

matrix = [list(map(str,input().split())) for _ in range(5)]

result = []
for i in range(5):
    for j in range(5):
        DFS(i, j, matrix[i][j])

print(len(result))
