def solution(n):
    board = [False, False] + [True]*(n-1)
    arr = []
    for i in range(2, n+1):
        if board[i]:
            arr.append(i)
            for j in range(2*i,n+1,i):
                board[j] = False
    return board.count(True)
