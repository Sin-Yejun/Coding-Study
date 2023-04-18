n, m = map(int, input().split())
arr1 = []
arr2 = []
for i in range(n):
    temp1 = list(map(int, input().split()))
    arr1.append(temp1)
for j in range(n):
    temp2 = list(map(int, input().split()))
    arr2.append(temp2)

for k in range(n):
    ans = [a1+b1 for a1, b1 in zip(arr1[k],arr2[k])]
    print(' '.join(map(str,ans)))
