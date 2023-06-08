import sys
input = sys.stdin.readline

MOD = 1000000007

def calculate_inverse(num):
    return pow(num, MOD - 2, MOD)

M = int(input())
expectation = 0

for _ in range(M):
    N, S = map(int, input().split())
    numerator = 1
    denominator = 1

    denominator = (denominator * calculate_inverse(N)) % MOD
    numerator = (numerator * S) % MOD

    expectation = (expectation + numerator * denominator) % MOD

print(expectation)
