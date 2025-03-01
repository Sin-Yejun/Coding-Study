nanjang = [int(input()) for _ in range(9)]

l = len(nanjang)
check = False
wrong = []
for i in range(9):
    total = sum(nanjang)
    for j in range(9):
        if i != j:
            if total - (nanjang[i] + nanjang[j]) == 100:
                wrong.append(nanjang[i])
                wrong.append(nanjang[j])
                check = True
                break
    if check:
        break

for i in nanjang:
    if i not in wrong:
        print(i)