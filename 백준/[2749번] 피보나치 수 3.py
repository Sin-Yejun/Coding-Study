# 피보나치를 구하는 가장 빠른 방법 = 행렬거듭제곱 (n이 클 때)

import sys
sys.setrecursionlimit(10**6)
def matrix_mult_mod(A, B, mod):
    # 행렬 곱셈 후 모듈러 적용
    result = [[0, 0], [0, 0]]
    result[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % mod
    result[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % mod
    result[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % mod
    result[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % mod
    return result

def matrix_power_mod(M, n, mod):
    # 단위 행렬
    result = [[1, 0], [0, 1]]
    base = [row[:] for row in M]  # M 깊은 복사
    power = n
    
    while power > 0:
        if power % 2 == 1:
            result = matrix_mult_mod(result, base, mod)
        base = matrix_mult_mod(base, base, mod)
        power //= 2
    
    return result

def fib_mod(n, mod):
    if n <= 0: return 0
    if n == 1: return 1
    
    M = [[1, 1], [1, 0]]
    F = [1, 0]
    
    # n-1 거듭제곱 계산
    result = matrix_power_mod(M, n-1, mod)
    return (result[0][0] * F[0] + result[0][1] * F[1]) % mod

# 테스트
n = int(input().strip())
mod = 1000000
print(fib_mod(n, mod))