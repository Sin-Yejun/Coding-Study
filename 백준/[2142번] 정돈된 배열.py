# https://jeonggyun.tistory.com/298
T = int(input())
for _ in range(T):
    n, m = map(int,input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int,input().split())))

    ans = 1
    for i in range(1, n):
        for j in range(1, m):
            if arr[i-1][j-1] + arr[i][j] > arr[i-1][j] + arr[i][j-1]:
                ans = 0
    if ans:
        print('YES')
    else:
        print('NO')


