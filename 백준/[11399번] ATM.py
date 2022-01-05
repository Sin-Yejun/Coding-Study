n = int(input())
arr = list(map(int,input().split()))
arr.sort()
s = 0
for i in range(1,n):
    s+=sum(arr[:i])
print(s+sum(arr))
