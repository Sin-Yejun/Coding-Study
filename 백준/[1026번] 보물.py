n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
s = 0
for i in range(n):
    s+= min(A)*max(B)
    A.remove(min(A))
    B.remove(max(B))
    

print(s)
