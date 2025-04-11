n, m = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))

temp = []

def dfs():
    if len(temp) == m:
        print(' '.join(map(str, temp)))
        return
    for i in range(len(arr)):
        temp.append(arr[i])
        dfs()
        temp.pop()

dfs()