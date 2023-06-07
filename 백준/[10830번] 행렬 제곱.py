import sys
input = sys.stdin.readline
def matrix_multiply(A, B):
    # 행렬 A와 B의 곱을 계산하여 반환하는 함수
    N = len(A)
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= 1000
    return result

def matrix_power_mod(A, B):
    # 주어진 행렬 A를 B번 거듭제곱하여 반환하는 함수
    N = len(A)
    # 초기 행렬은 단위 행렬로 설정
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        result[i][i] = 1
    while B > 0:
        if B % 2 == 1:
            result = matrix_multiply(result, A)
        A = matrix_multiply(A, A)
        B //= 2
    return result

# 입력값 받기
N, B = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

# 초기 행렬 생성
A = matrix

# 행렬 제곱 결과 출력
result = matrix_power_mod(A, B)
for row in result:
    print(' '.join(map(str, row)))
