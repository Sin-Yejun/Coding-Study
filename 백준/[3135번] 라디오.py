A, B = map(int,input().split())
Min = abs(A-B)-1
n = int(input())
for _ in range(n):
    k = int(input())
    if abs(B-k) < Min:
        Min = abs(B-k)

print(Min+1)
