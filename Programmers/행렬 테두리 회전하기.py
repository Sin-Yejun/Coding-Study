def solution(rows, columns, queries):
    arr = [[0 for i in range(columns+1)] for j in range(rows+1)]
    idx = 1
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            arr[i][j] = idx
            idx += 1
    answer = []
    for x1, y1, x2, y2 in queries:
        first = arr[x1][y1]
        Min = first
        for i in range(x1, x2):
            tmp = arr[i+1][y1]
            arr[i][y1] = tmp
            Min = min(Min,tmp)
        for i in range(y1, y2):
            tmp = arr[x2][i+1]
            arr[x2][i] = tmp
            Min = min(Min,tmp)
        for i in range(x2,x1,-1):
            tmp = arr[i-1][y2]
            arr[i][y2] = tmp
            Min = min(Min,tmp)
        for i in range(y2,y1,-1):
            tmp = arr[x1][i-1]
            arr[x1][i] =tmp
            Min = min(Min,tmp)
    
        arr[x1][y1+1] = first
        answer.append(Min)
    return answer
