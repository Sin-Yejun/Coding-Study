# https://happylsm76.tistory.com/entry/%EB%B0%B1%EC%A4%80-2630%EB%B2%88%EC%83%89%EC%A2%85%EC%9D%B4-%EB%A7%8C%EB%93%A4%EA%B8%B0-with-Python
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

result = []

def solution(x, y, n):
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != arr[i][j]:
                solution(x,y,n//2)
                solution(x,y+n//2,n//2)
                solution(x+n//2,y,n//2)
                solution(x+n//2,y+n//2,n//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

solution(0,0,n)
print(result.count(0))
print(result.count(1))
