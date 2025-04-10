from collections import defaultdict
n, k = map(int, input().split())
arr = list(map(int, input().split()))

d = defaultdict(int)
left = 0
max_len = 0
for right in range(n):
    d[arr[right]] += 1

    while d[arr[right]] > k:
        d[arr[left]] -= 1
        left += 1
    
    max_len = max(max_len, right-left+1)
print(max_len)