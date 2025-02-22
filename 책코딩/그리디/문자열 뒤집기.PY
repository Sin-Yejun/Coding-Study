n = input()
pre = -1
cnt0 = 0
# 1로 만들기
for i in n:
    if i == '0':
        if pre == 0:
            continue
        cnt0 += 1
        pre = 0
    else:
        pre = 1
# 0으로 만들기
pre = -1
cnt1 = 0
for i in n:
    if i == '1':
        if pre == 1:
            continue
        cnt1 += 1
        pre = 1   
    else:
        pre = 0
print(min(cnt0, cnt1))