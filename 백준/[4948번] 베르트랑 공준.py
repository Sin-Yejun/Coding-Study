prime_list = [False,False]+[True]*1000000
for i in range(2,int(1000000**0.5)+1):
    if prime_list[i] == True:
        for j in range(i*2,len(prime_list),i):
            prime_list[j] = False
while True:
    n = int(input())
    if n==0:
        break
    count = 0
    for i in range(n+1,2*n+1):
        if prime_list[i]==True:
            count +=1
    print(count)


