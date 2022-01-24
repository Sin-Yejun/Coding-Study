class Solution:
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        def check(matrix):
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] == 0:
                        return True
            return False
        
        row = len(matrix)
        col = len(matrix[0])
        visited = [[0]*col for i in range(row)]
        ans = []
        # left: [0,1], down:[1,0], right: [0,-1], up: [-1,0]
        move = [0, 1]
        y = 0
        x = 0
        while check(visited):
            if col == 1:
                ans.append(matrix[y][x])
                visited[y][x] = 1
                y+=1
            else:
                if visited[y][x] == 0:
                    ans.append(matrix[y][x])
                    visited[y][x] = 1
                else:
                    if move == [0,1]:       # left -> down
                        x-= 1
                        move = [1,0]
                    elif move == [1,0]:     # down -> right
                        y -= 1
                        move = [0,-1]
                    elif move == [0,-1]:    # right -> up
                        x += 1
                        move = [-1,0]
                    elif move == [-1,0]:    # up -> left
                        y += 1
                        move = [0,1]

                x += move[1]
                y += move[0]
                if x == col-1 and y == 0:
                    move = [1,0]
                if y == row-1 and x == col-1:
                    move = [0,-1]
                if x == 0 and y == row-1:
                    move = [-1, 0]
                if x == 0 and y == 1:
                    move = [0,1]
        return ans
