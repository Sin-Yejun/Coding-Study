n = int(input())

for k in range(n):
    a = int(input())
    b = int(input())
    list1 = [i for i in range(1,b+1)]
    for i in range(a):
        for j in range(1,b):
            list1[j]+=list1[j-1]
    print(list1[-1])


