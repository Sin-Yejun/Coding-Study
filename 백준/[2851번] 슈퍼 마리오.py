total = 0
arr = []
for i in range(10):
    arr.append(int(input()))
for i in arr:
    total += i
    if total >= 100:
        break

if abs(total-100) <= abs( (total-i) - 100):
    print(total)
else:
    print(total-i)
    
