def solution(board, skill):
    arr = [[0 for i in range(len(board[0])+1)] for j in range(len(board)+1)]
    for s in skill:
        x1, y1 = s[1], s[2]
        x2, y2 = s[3], s[4]
        v = s[5]
        if s[0] == 1:
            arr[x1][y1] -= v
            arr[x1][y2+1] += v
            arr[x2+1][y1] += v
            arr[x2+1][y2+1] -= v
        elif s[0] == 2:
            arr[x1][y1] += v
            arr[x1][y2+1] -= v
            arr[x2+1][y1] -= v
            arr[x2+1][y2+1] += v
    tmp = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            tmp += arr[i][j]
            arr[i][j] = tmp
        tmp = 0
    tmp = 0
    for i in range(len(arr[0])):
        for j in range(len(arr)):
            tmp += arr[j][i]
            arr[j][i] = tmp
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + arr[i][j] > 0:
                cnt += 1
    return cnt
            
