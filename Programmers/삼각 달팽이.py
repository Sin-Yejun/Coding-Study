def solution(n):
    arr = []
    for i in range(1, n+1):
        arr.append([0 for j in range(i)])
    
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i,n):
            if i % 3 == 0:      # 아래
                x += 1
            elif i % 3 == 1:    # 오른쪽
                y += 1
            else:               # 위
                x-= 1
                y-= 1
            arr[x][y] = num
            num += 1
    return sum(arr,[])
