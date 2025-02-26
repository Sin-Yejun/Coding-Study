def solution(key, lock):
    m = len(key)
    n = len(lock)
    # ans = sum([1 for x in lock if x == 0])
    extend = [[0]*(n+2*(m-1)) for _ in range(n+2*(m-1))]
    
    for i in range(n):
        for j in range(n):
            extend[m-1+i][m-1+j] = lock[i][j]
    
    def rotate90(mat):
        return list(zip(*mat[::-1]))
    
    def check(offsetX, offsetY):
        temp_lock = [row[:] for row in extend]  # 복사본을 사용해야 함
        for i in range(m):
            for j in range(m):
                temp_lock[offsetX+i][offsetY+j] += key[i][j]  # temp_lock에 적용해야 함
        for i in range(n):
            for j in range(n):
                if temp_lock[m-1+i][m-1+j] != 1:  # lock 부분만 확인
                    return False
        return True

    
    for i in range(4):
        key = rotate90(key)
        for i in range(n+m-1):
            for j in range(n+m-1):
                if check(i, j):
                    return True  # 맞춰지면 즉시 True 반환
    return False  # 끝까지 안되면 False
            