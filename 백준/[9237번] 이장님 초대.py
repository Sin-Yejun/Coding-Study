n = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse = True)
for i in range(1,n+1):
    arr[i-1] = arr[i-1] +i

print(max(arr)+1)
