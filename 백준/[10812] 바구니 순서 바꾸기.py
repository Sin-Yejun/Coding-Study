n, m = map(int, input().split())
arr = [x for x in range(1, n+1)]
for _ in range(m):
    i, j, k = map(int, input().split())
    rot_arr = arr[k-1:j] + arr[i-1:k-1]
    for y in rot_arr:
        arr[i-1] = y
        i += 1
print(' '.join(map(str,arr)))
