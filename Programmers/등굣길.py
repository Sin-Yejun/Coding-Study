def solution(m, n, puddles):
    arr = [[0 for i in range(m)] for i in range(n)]
    arr[0][0] = 1
    
    for y, x in puddles:
        arr[x-1][y-1] = -1
        
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if arr[i][j] == -1:
                arr[i][j] = 0
                continue
            if i == 0:
                arr[i][j] = arr[i][j-1]
            elif j == 0:
                arr[i][j] = arr[i-1][j]
            else:
                arr[i][j] = (arr[i-1][j] + arr[i][j-1]) % 1000000007
    return arr[n-1][m-1]
