import sys
while True:
    a, b = map(int,sys.stdin.readline().split())
    if a==0 and b==0:
        break
    if a==0 or b ==0:
        print('neither')
    elif a % b == 0:
        print('multiple')
    elif b % a == 0:
        print('factor')
    else:
        print('neither')
    
