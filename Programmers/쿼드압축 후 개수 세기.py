def solution(arr):
    def QuadTree(data,x,y, size):
        temp = data[x][y]
        Flag = True
        for i in range(x,x+size):
            for j in range(y, y+size):
                if data[i][j] != temp:
                    Flag = False
                    break
            if Flag == False: break
        if Flag == True:
            cnt[temp] += 1
            return
        half_size = size // 2
        QuadTree(data,x,y, half_size)
        QuadTree(data,x+half_size,y, half_size)
        QuadTree(data,x,y+half_size, half_size)
        QuadTree(data,x+half_size,y+half_size, half_size)
    cnt = [0,0]
    QuadTree(arr,0,0, len(arr))
    return cnt
