def self(n):
    s=n
    while(1):
        s+=n%10
        n=n//10
        if(n<=0 or s>10000):
            break
    return s

list1 = [False for i in range(10001)]

for i in range(10000):
    idx = self(i)
    if idx< 10001:
        list1[idx]=True
ct=0
for j in list1:
    if j == False:
        print(ct)
    ct+=1



    
