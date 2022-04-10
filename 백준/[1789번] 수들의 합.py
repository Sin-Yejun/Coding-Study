s = int(input())
temp = 1
n = 0
while s!=0:
    if s - temp < 0:
        break
    s -= temp
    temp += 1
    n += 1

print(n)    
