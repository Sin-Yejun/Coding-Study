# https://my-coding-notes.tistory.com/267
import sys
input = sys.stdin.readline

sudoku = [list(map(int,list(input().rstrip().split()))) for _ in range(9)]
zeros = [(i,j) for i in range(9) for j in range(9) if not sudoku[i][j]]
cand = [i for i in range(1,10)]

def bt(n):
    if n == len(zeros):
        for i in sudoku:
            print(*i,sep=" ")
        sys.exit()
        
    x,y = zeros[n]
    a,b = x//3,y//3
    cand2 = cand[:]
    
    # 박스 칸
    for i in range(3*a,(a+1)*3):
        for j in range(3*b,(b+1)*3):
            if sudoku[i][j] in cand2:
                cand2.remove(sudoku[i][j])
    
    # 가로 세로
    for i in range(9):
        if sudoku[x][i] in cand2:
            cand2.remove(sudoku[x][i])
        if sudoku[i][y] in cand2:
            cand2.remove(sudoku[i][y])
    
    for i in cand2:
        sudoku[x][y] = i
        bt(n+1)
    sudoku[x][y] = 0

if __name__ == '__main__':
    bt(0)
