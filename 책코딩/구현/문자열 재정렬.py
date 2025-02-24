string = input()
alpha = []
num = []
for x in string:
    if x.isnumeric():
        num.append(int(x))
    else:
        alpha.append(x)

alpha.sort()
print(''.join(alpha)+str(sum(num)))