n = int(input())
cnt = 0
pass_flag = False
m = n
if m%5 == 0:
    cnt = m//5
else:
    if m<5 and m%3 != 0:
        cnt = -1
    elif m == 3:
        cnt = 1
    else:
        if m>5:
            temp = m//5
            while 1:
                m = n
                m -= (5*temp)
                if m % 3 == 0:
                    cnt += temp
                    cnt += m//3
                    pass_flag = True
                    break
                temp -= 1
                if temp < 0:
                    break
            if pass_flag == False:
                m = n
                if m % 3 == 0:
                    cnt += n//3
                else:
                    cnt = -1
print(cnt)
