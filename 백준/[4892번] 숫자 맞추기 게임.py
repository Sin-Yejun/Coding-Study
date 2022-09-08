import sys
input = sys.stdin.readline
cnt = 0
while True:
    even = True
    n = int(input())
    cnt += 1
    if n == 0:
        break
    n1 = n*3
    if n1 % 2 == 1:
        even = False
    if even:
        n2 = n1//2
    else:
        n2 = (n1+1)//2
    n3 = 3*n2
    n4 = n3//9
    if even:
        print(str(cnt)+'.','even',n4)
    else:
        print(str(cnt)+'.','odd',n4)
