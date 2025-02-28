import datetime
y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())

checkgg = False
if y1 + 1000 < y2:
    checkgg = True
elif y1 + 1000 == y2:
    if m1 < m2:
        checkgg = True
    elif m1 == m2:
        if d1 <= d2:
            checkgg = True
if checkgg:
    print('gg')
    exit(0)
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

time1 = datetime.date(year=y1, month= m1, day= d1)
time2 = datetime.date(year=y2, month= m2, day= d2)
x = time2 - time1
print('D-'+str(x.days))