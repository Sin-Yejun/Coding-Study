import sys
def fibo(n):
    fib = [0,1]
    for i in range(2, n):
        fib.append(fib[i-1]+fib[i-2])
    return fib

a = int(input())
for _ in range(a):
    n = int(sys.stdin.readline())
    if n == 0:
        print(1,0)
    elif n == 1:
        print(0,1)
    else:
        arr = fibo(n)
        print(arr[-1], arr[-1]+arr[-2])
    
