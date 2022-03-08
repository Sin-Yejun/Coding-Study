n = int(input())

T = 0
cnt = 1

for _ in range(n):
    a, b, t = map(int,input().split())
    T = T ^ t
    cnt = cnt // a * b
print(T, cnt)
            
    
