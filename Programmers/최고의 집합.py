n = 2
s = 1
temp = []
while s > 0:
    x = s // n
    s -= x
    n -= 1
    temp.append(x)
print(temp)