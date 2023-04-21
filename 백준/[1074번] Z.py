def visit(N, r, c):
    if N == 0: # N이 0이면 첫번째 방문을 반환
        return 0
    
    # 한 변의 크기가 2^(N-1)인 작은 정사각형의 크기
    size = 2 ** (N-1)
    
    if r < size and c < size: # 왼쪽 위
        return visit(N-1, r, c)
    elif r < size and c >= size: # 오른쪽 위
        return size**2 + visit(N-1, r, c-size)
    elif r >= size and c < size: # 왼쪽 아래
        return 2*size**2 + visit(N-1, r-size, c)
    else: # 오른쪽 아래
        return 3*size**2 + visit(N-1, r-size, c-size)

n, r, c = map(int, input().split())
print(visit(n, r, c))
