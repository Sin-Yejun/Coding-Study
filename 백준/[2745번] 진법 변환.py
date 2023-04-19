import math
N, B = input().split()
exponent = len(N)-1
B = int(B)
ans = 0
for i in N:
    if i.isdigit():
        ans += math.pow(B, exponent) * int(i)
    else:
        ans += math.pow(B, exponent) * (ord(i)-55)
    exponent -= 1

print(int(ans))
