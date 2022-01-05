k = int(input())
for _ in range(k):
    n= int(input())
    prime_list = [False,False]+[True]*(n+1)

    for i in range(2,int(n**0.5)+1):
        if prime_list[i] == True:
            for j in range(i*2,len(prime_list),i):
                prime_list[j] = False
    l = []
    for i in range(1,n):
        if prime_list[i]==True:
            if prime_list[n-i] == True:
                l.append((i, n-i, abs(i-(n-i))))
    l.sort(key = lambda x:x[2])
    print(l[0][0], l[0][1])
