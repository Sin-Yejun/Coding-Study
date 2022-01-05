#에라토스테네스의 체 이용
n, m = map(int,input().split())
prime_list = [False,False]+[True]*(m+1)

for i in range(2,int(m**0.5)+1):
    if prime_list[i] == True:
        for j in range(i*2,len(prime_list),i):
            prime_list[j] = False

for i in range(n,m+1):
    if prime_list[i]==True:
        print(i)
