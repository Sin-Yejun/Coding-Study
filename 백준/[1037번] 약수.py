n = int(input())
arr = list(map(int,input().split()))
arr.sort()
if len(arr)==1:
    print(arr[0]**2)
else:
    print(arr[0]*arr[-1])
