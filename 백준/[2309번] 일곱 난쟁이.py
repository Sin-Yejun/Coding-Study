arr = []
for i in range(9):
    n = int(input())
    arr.append(n)
for i in range(8):
    for j in range(i+1,9):
        if sum(arr)-arr[i]-arr[j] == 100:
            r1 = arr[i]
            r2 = arr[j]
            break
arr.remove(r1)
arr.remove(r2)
arr.sort()
for i in arr:
    print(i)
