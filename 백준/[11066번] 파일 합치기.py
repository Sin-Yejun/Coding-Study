import sys
input = sys.stdin.readline
INF = float('inf')
T = int(input())
for _ in range(T):
    k = int(input())
    arr = list(map(int, input().split()))
    # 누적합 배열 만들기
    prefix = [0] * (k + 1)
    for i in range(1, k+1):
        prefix[i] = prefix[i-1] + arr[i-1]

    # dp[i][j] = i번 파일부터 j번 파일까지 '하나로 합치는 데 드는 최소 비용'
    dp = [[0]*(k+1) for _ in range(k+1)]

    for length in range(2, k+1):  # 파일 묶는 길이: 2개부터 k개까지
        for i in range(k - length + 1):  # 시작점
            j = i + length - 1  # 끝점
            dp[i][j] = INF  # 최소값 비교할 거니까 INF로 초기화

            for mid in range(i, j):  # i~j 사이를 mid로 끊음
                dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid+1][j] + prefix[j+1] - prefix[i])
    print(dp[0][k-1])