def hansu(n):
    if 1<=n<=99:
        return True
    a = [0,0,0]
    b = n
    i=0
    if n==1000:
        return False
    while(b>0):
        a[i] = b%10
        b = b//10
        i+=1
    if a[2]-a[1]==a[1]-a[0]:
        return True
    return False

k = int(input())
ct=0
for i in range(1,k+1):
    l = hansu(i)
    if l==True:
        ct+=1
print(ct)


    
