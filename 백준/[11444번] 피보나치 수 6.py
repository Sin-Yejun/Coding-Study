def fibo(n):
    if n < 0:
        raise ValueError("n must be non-negative")

    # 행렬 거듭제곱을 이용하여 n번째 피보나치 수를 계산하는 함수
    def matrix_pow(matrix, n):
        if n == 1:
            return matrix
        elif n % 2 == 0:
            temp = matrix_pow(matrix, n//2)
            return multiply_matrices(temp, temp)
        else:
            temp = matrix_pow(matrix, (n-1)//2)
            return multiply_matrices(multiply_matrices(temp, temp), matrix)

    # 두 개의 2x2 행렬을 곱하는 함수
    def multiply_matrices(matrix1, matrix2):
        a = (matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0]) % 1000000007
        b = (matrix1[0][0] * matrix2[0][1] + matrix1[0][1] * matrix2[1][1]) % 1000000007
        c = (matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0]) % 1000000007
        d = (matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1]) % 1000000007
        return [[a, b], [c, d]]

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        matrix = [[1, 1], [1, 0]]
        result_matrix = matrix_pow(matrix, n-1)
        return result_matrix[0][0]

n = int(input())
print(fibo(n))
