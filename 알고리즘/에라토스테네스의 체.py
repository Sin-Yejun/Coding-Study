def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)  # 처음에는 모든 숫자를 소수(True)로 가정
    primes[0], primes[1] = False, False  # 0과 1은 소수가 아님

    for i in range(2, int(n**0.5) + 1):
        if primes[i]:  # i가 소수라면
            for j in range(i * i, n + 1, i):  # i의 배수를 모두 제거
                primes[j] = False

    return [i for i, prime in enumerate(primes) if prime]

# 예제: 50 이하의 소수 찾기
print(sieve_of_eratosthenes(50))
