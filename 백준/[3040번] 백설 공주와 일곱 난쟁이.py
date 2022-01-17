li = []

for i in range(9):
    li.append(int(input()))

s = sum(li) - 100
# (난쟁이 모자의 숫자 합) - 100 = (가짜 난쟁이 모자 숫자 합)

for i in li:
    if s-i in li:
        a, b = i, s-i
        break

li.remove(a)
li.remove(b)

for i in li:
    print(i)
