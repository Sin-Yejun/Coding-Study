def solution(board, moves):
    ans = []
    cnt = 0
    for idx in moves:
        for i in range(len(board[0])):
            if board[i][idx-1] != 0:
                ans.append(board[i][idx-1])
                board[i][idx-1] = 0
                if len(ans) > 1 and ans[-1] == ans[-2]:
                    ans = ans[:len(ans)-2]
                    cnt += 2
                break
    return cnt
