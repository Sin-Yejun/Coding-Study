n = input()
arr = list(map(int,n))
if 0 not in arr:
    print(-1)
else:
    arr.remove(0)
    if sum(arr)%3 != 0:
        print(-1)
    else:
        arr.sort(reverse=True)
        arr.append(0)
        print(''.join(map(str,arr)))
