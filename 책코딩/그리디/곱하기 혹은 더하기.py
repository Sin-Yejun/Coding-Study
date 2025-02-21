s = input()
result = 0
for i in s:
    i = int(i)
    if result == 0 or i == 0 or i == 1:
        result += i
    else:
        result *= i
print(result)
        