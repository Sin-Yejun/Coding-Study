n = int(input())
arr = list(map(int, input().split()))

d = [0]*100
d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+d[i])
print(d[n-1])