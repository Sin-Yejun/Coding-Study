arr = list(map(int,input().split()))
total = 0
for i in arr:
    total += i**2
print(total%10)
