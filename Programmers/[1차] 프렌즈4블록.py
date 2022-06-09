def return_xy(m,n,board):   # 2*2 형태로 사라질 블록의 왼쪽위 블럭의 좌표값 리턴
    arr = []
    for i in range(m):
        for j in range(n):
            if i+1 < m and j+1 < n:
                if board[i][j] and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                # 왼쪽위 블록 기준으로 그 값이 0이 아니고 오른쪽, 아래, 오른쪽 아래 블록의 값이 값으면 좌표값 저장
                    arr.append([i,j])
    return arr
def check(m,n, board):      # 2*2 형태로 사라질 블록이 있는지 확인
    for i in range(m):
        for j in range(n):
            if i+1 < m and j+1 < n:
                if board[i][j] and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    return True
    return False

def compression(arr):       # 2*2블럭의 값이 0(빈공간)으로 채워지고 그 위의 블럭이 빈공간을 매꿈
    # Transpose 된 배열을 처리
    # 예를 들어, ['T',0,0,'T','T','T'] 인 열을 [0,0, 'T','T','T','T'] 형태로 만들어줌
    new_arr = []
    for i in arr:
        cnt = i.count(0)
        if cnt == 0:
            new_arr.append(i)
            continue
        temp = []
        for j in i:
            if j != 0:
                temp.append(j)
        temp = [0]*cnt + temp
        new_arr.append(temp)
    return new_arr

def Transpose(arr):     # compression 함수를 쉽게 하기 위해 행과 열을 바꿔줌
    A = list(zip(*arr)) # Transpose 시키는 방법
    new_arr = []        # Tuple은 값을 바꿀 수 없어 다시 List 형태로 저장해줌
    for i in A:
        new_arr.append(list(i))
    return new_arr

def solution(m, n, board):
    # 기존의 board 형태는 문자열 배열로 값을 변경 할 수 없으므로 character 배열로 바꿔줌
    # 예) ["TA", "TT"] -> [['T', 'A'], ['T', 'T']]
    board = [list(i) for i in board]    
    
    if not check(m,n, board):   # 2*2 형태로 지워질 블록이 없다면 return 0
        return 0
    while check(m,n, board):    # 2*2 형태로 지워질 블록이 있다면
        
        arr = return_xy(m,n, board) # 사라져야 할 블록의 왼쪽위 블록의 좌표값을 얻어옴 
        
        for x,y in arr:         # 지워질 블록의 값을 0으로 바꿔줌
            board[x][y] = 0
            board[x][y+1] = 0
            board[x+1][y] = 0
            board[x+1][y+1] = 0
            
        board_T = Transpose(board)      # 압축을 쉽게하기 위해 행과 열을 바꿔줌
        board_T = compression(board_T)  # 압축
        board = Transpose(board_T)      # 다시 원상태로 바꿔줌
    
    # board에 지워진 블록이 몇개인지 count 함
    cnt = sum([board[i].count(0) for i in range(len(board))])
    
    # 답 return
    return cnt
    
