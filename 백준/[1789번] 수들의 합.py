s = int(input())
total = 0
count= 1
while True:
    if total>=s:
        break
    total += count
    if total>s:
        total -= count
        count +=2
    else:
        count += 1
    print(total)
print(count)
