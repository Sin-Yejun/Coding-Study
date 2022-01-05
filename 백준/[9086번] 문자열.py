n = int(input())
for _ in range(n):
    s = input()
    if len(s) < 2:
        print(s*2)
    else:
        print(s[0]+s[-1])
