n = int(input())
cnt=0
for i in range(2*n-1):
    if i<n:
        print(' '*i,end='')
        print('*'*(2*(n-i)-1))
    else:
        cnt+=1
        print(' '*(n-cnt-1),end='')
        print('*'*(2*cnt+1))
    
