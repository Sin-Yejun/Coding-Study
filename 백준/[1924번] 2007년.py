x, y = map(int,input().split())
date = [31,28,31,30,31,30,31,31,30,31,30,31]
day = ['SUN','MON','TUE','WED','THU','FRI','SAT']

index = 0
if x==1:
    index = y
else:
    for i in range(x-1):
        index += date[i]
    index += y

print(day[index%7])
        
