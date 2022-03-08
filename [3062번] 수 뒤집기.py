n = int(input())

for _ in range(n):
    num = input()
    s = int(num) + int(num[::-1])
    s = str(s)
    check = 1
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            check = 0
    if check:
        print('YES')
    else:
        print('NO')
        
