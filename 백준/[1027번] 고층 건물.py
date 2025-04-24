import sys
input = sys.stdin.readline


n = int(input())
h = list(map(int, input().split()))
answer = 0

for i in range(n):
    visible = 0
    # 왼쪽 보기
    max_slope = float('-inf')
    for j in range(i - 1, -1, -1):
        slope = (h[j] - h[i]) / (i - j)
        if slope > max_slope:
            max_slope = slope
            visible += 1

    # 오른쪽 보기
    max_slope = float('-inf')
    for j in range(i + 1, n):
        slope = (h[j] - h[i]) / (j - i)
        if slope > max_slope:
            max_slope = slope
            visible += 1

    answer = max(answer, visible)

print(answer)
