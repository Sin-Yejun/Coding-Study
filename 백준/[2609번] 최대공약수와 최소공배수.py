#유클리드 호제법 이용
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
a, b = map(int,input().split())
gcd = gcd(a,b)
print(gcd)
print(a*b//gcd)
