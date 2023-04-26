n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [0]*n
def dfs(x):
    for i in range(n):
        if visited[i] == 0 and arr[x][i] == 1:
            visited[i] = 1
            dfs(i)
            
for i in range(n):
    dfs(i)
    for j in range(n):
        if visited[j]:
            print(1, end = ' ')
        else:
            print(0, end = ' ')
    print()
    visited = [0]*n

    
