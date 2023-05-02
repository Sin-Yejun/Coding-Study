import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))
ans = []
def dfs(depth):
    if depth == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(len(arr)):
        if depth == 0 or ans[-1] <= arr[i]:
            ans.append(arr[i])
            dfs(depth+1)
            ans.pop()
dfs(0)
