n = int(input())

for i in range(n):
    if i==n-1:
        print('*'*(2*n-1))
    else:
        print(' '*(n-1-i),end='')
        print('*',end='')
        if i!=0:
            print(' '*(i*2-1),end='')
            print('*')
        else:
            print(' '*(i*2-1))
        
