a, b = map(int,input().split())

result = a
if b-a < 10:
    for i in range(a+1, b+1):
        result ^= i
else:
    for i in range(a+1, b+1):
        if i % 4 == 0:
            break
        result ^= i
    for i in range(b, a-1, -1):
        if (i+1)%4==0:
            break
        result ^= i
print(result)
