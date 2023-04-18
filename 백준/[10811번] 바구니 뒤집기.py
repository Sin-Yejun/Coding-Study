n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    rev_arr = list(reversed(arr[x-1:y]))
    for k in rev_arr:
        arr[x-1] = k
        x += 1
print(' '.join(map(str,arr)))
    
