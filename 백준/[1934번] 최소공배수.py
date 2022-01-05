#유클리드 호제법 이용
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
n = int(input())
for _ in range(n):
    a, b = map(int,input().split())
    c = gcd(a,b)
    print(a*b//c)
    
