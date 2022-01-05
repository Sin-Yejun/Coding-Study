n = int(input())
cnt = 0
for i in range(2*n-1):
    if i<n:
        print(' '*(n-1-i),end='')
        print('*'*(2*(i+1)-1))
    else:
        cnt +=1
        print(' '*cnt,end='')
        print('*'*((2*n-1)-(2*cnt)))
