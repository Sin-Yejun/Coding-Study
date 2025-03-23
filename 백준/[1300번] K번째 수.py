n = int(input())  # 곱셈표의 크기 (n x n)
k = int(input())  # 찾고자 하는 k번째 수

left = 1  # 이진 탐색의 시작 값 (가장 작은 곱셈표의 값)
right = k + 1  # 이진 탐색의 끝 값 (최대 k번째 수는 k 이하이므로 k+1로 설정)

# 이진 탐색 시작
while left <= right:
    mid = (left + right) // 2  # 중간값 계산 (현재 후보 숫자)
    cnt = 0  # mid 이하의 숫자가 곱셈표에 몇 개 있는지 세기 위한 변수

    # 곱셈표의 각 행마다 mid 이하의 수가 몇 개인지 계산
    for i in range(1, n + 1):
        # i번째 행에는 i, 2i, 3i, ..., ni 가 있음
        # mid // i 는 i로 나누었을 때 mid 이하의 배수 개수
        # 단, 한 행에는 최대 n개까지만 존재하므로 min 사용
        cnt += min(mid // i, n)

    # mid 이하의 수가 k개 이상이라면, 정답은 mid보다 작거나 같을 수 있음
    if cnt >= k:
        right = mid - 1  # 범위를 왼쪽으로 좁힘
    else:
        left = mid + 1  # mid보다 더 큰 값에서 찾아야 함

# 반복이 끝난 후, left는 정확히 K번째 수를 가리킴
print(left)
