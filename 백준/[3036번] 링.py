def GCD(a,b):
    while b!=0:
        a , b = b, a%b
    return a
n = int(input())
arr = list(map(int,input().split()))

divisor = arr[0]
for i in range(1, n):
    a = divisor // arr[i]
    b = divisor % arr[i]
    if b==0:
        print(str(a)+'/1')
    else:
        g = GCD(divisor,arr[i])
        a = divisor // g
        b = arr[i] // g
        print(str(a)+'/'+str(b))
