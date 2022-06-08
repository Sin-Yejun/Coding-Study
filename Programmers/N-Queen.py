def dfs(queen, row, n):
    count = 0
    if n == row:
        return 1
    for col in range(n):
        queen[row] = col
        for i in range(row):
            if queen[i] == queen[row]:  # 같은 열에 있다면 Break
                break
            if abs(queen[i]-queen[row]) == row - i: # 대각선에 겹친다면
                break
        else:
            count += dfs(queen, row + 1, n)
    return count

def solution(n):
    return dfs([0]*n,0,n)
