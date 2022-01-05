n = int(input())
flag = True
for i in range(1,n):
    if i + sum(map(int,str(i)))==n:
        flag = False
        print(i)
        break
if flag == True:
    print(0)

