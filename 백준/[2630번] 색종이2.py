n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
result = []
def solution(x,y,n):
    color = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j] != color:
                solution(x, y, n//2)
                solution(x+n//2, y, n//2)
                solution(x, y+n//2, n//2)
                solution(x+n//2, y+n//2, n//2)
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)
solution(0,0,n)
print(result.count(0))
print(result.count(1))
                
