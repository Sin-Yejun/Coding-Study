import sys
n = int(input())
arr = [0]*10001
for _ in range(n):
    num = int(sys.stdin.readline())
    arr[num] += 1
for i in range(10001):
    if arr[i]!=0:
        for _ in range(arr[i]):
            print(i)





''' 메모리 초과
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr2 = [0]*(max(arr)+1)

for i in arr:
    arr2[i] += 1
for i in range(len(arr2)-1):
    arr2[i+1] += arr2[i]
output = [-1]*len(arr)
for i in arr:
    output[arr2[i]-1] = i
    arr2[i] -= 1
print('\n'.join(map(str,output)))
'''
