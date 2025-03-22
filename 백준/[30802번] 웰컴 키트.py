import math
n = int(input())
l = list(map(int, input().split()))
t, p =map(int, input().split())
a = 0

for count in l:
    a += math.ceil(count/t)

print(a)
print(n//p, n%p)

