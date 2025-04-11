n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

tmp = []
def dfs(start):
    prev = -1
    if len(tmp) == m:
        print(' '.join(map(str, tmp)))
        return
    for i in range(start, len(arr)):
        if arr[i] == prev:  # 이전에 썼던 숫자면 skip
            continue
        prev = arr[i]
        tmp.append(arr[i])
        dfs(i+1)
        tmp.pop()

dfs(0)
