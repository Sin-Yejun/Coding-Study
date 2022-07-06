n = int(input())
arr = [ list(map(int,input())) for i in range(n)]
result = []
def solution(x, y, n):
    num = arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if num != arr[i][j]:
                print('(',end='')
                solution(x,y,n//2)
                solution(x,y+n//2,n//2)
                solution(x+n//2,y,n//2)
                solution(x+n//2,y+n//2,n//2)
                print(')',end='')
                return
    print(num,end='')
    

solution(0,0,n)
