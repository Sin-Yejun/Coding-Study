n = int(input())

for _ in range(n):
    arr = list(input())
    ans = 0
    for i in range(65, 91):
        if chr(i) not in arr:
            ans += i
    print(ans)
        
    
