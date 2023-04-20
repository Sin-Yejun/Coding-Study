import math
L = int(input())
s = input()
ans = 0
c = 0
for i in s:
    a = ord(i)-96
    ans += a*31**c
    c += 1
print(int(ans) % 1234567891)
