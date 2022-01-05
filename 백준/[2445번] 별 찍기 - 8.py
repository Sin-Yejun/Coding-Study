n = int(input())
cnt=0
for i in range(2*n-1):
    if i<n-1:
        print('*'*(i+1),end='')
        print(' '*((n-1-i)*2),end='')
        print('*'*(i+1))
    elif i==n-1:
        print('*'*(2*n))
    else:
        cnt+=2
        print('*'*(2*n-i-1),end='')
        print(' '*cnt,end='')
        print('*'*(2*n-i-1))
