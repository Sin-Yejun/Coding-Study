a, b = map(int,input().split())
time = int(input())

b = b + time
if b >= 60:
    temp = b // 60
    b = b % 60
    a += temp
if a >= 24:
    temp = a-24
    a = temp
print(a,b)
