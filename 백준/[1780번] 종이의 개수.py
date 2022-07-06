n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
result = [0,0,0]
def solution(x,y,n):
    color = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != arr[i][j]:
                solution(x,y,n//3)
                solution(x+n//3,y,n//3)
                solution(x,y+n//3,n//3)
                solution(x+n//3,y+n//3,n//3)
                solution(x+2*n//3,y,n//3)
                solution(x,y+2*n//3,n//3)
                solution(x+2*n//3,y+2*n//3,n//3)
                solution(x+2*n//3,y+n//3,n//3)
                solution(x+n//3,y+2*n//3,n//3)
                return
    result[color] += 1
solution(0,0,n)
print(result[-1])
print(result[0])
print(result[1])
