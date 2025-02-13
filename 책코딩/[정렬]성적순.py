n = int(input())
arr = []
for _ in range(n):
    temp = input().split()
    arr.append((temp[0],int(temp[1])))
arr = sorted(arr, key= lambda x : x[1])
for i in arr:
    print(i[0], end=' ')