def fibo(n):
    if n == 1 or n==0:
        return 1
    return n*fibo(n-1)

n = int(input())
print(fibo(n))
