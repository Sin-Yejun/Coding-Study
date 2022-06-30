n, k = map(int,input().split())
arr = list(map(int,input().split()))
sum = 0
for i in range(k):
    sum += arr[i]
max_sum = sum
start = 0
end = k
while end < n:
    temp = sum + arr[end] - arr[start]
    max_sum = max(max_sum, temp)
    end += 1
    start += 1
    sum = temp
print(max_sum)
