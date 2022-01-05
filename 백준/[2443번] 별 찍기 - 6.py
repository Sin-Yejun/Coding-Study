n = int(input())
for i in range(n):
    print(' '*i,end='')
    print('*'*(2*n-1-(2*i)))
