import math
def numerator(n, c):
    temp = 1
    for i in range(n, n- c, -1):
        temp *= i
    return temp
def denominator(c):
    return math.factorial(c)
n, m = map(int, input().split())
print(numerator(n, m)//denominator(m))
