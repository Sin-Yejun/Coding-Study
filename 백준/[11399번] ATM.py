n = int(input())
arr = list(map(int,input().split()))

arr.sort()
s = 0
for i in range(len(arr)):
    s += arr[i]
    for j in range(i):
        s += arr[j]

print(s)
    
        
