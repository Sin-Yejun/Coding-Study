def can_cross(stones, k, mid):
    cnt = 0  # 연속된 0의 개수
    for stone in stones:
        if stone - mid < 0:  # mid명이 건너면 부서지는 경우
            cnt += 1
            if cnt >= k:  # 연속된 k개가 부서지면 못 건넘
                return False
        else:
            cnt = 0  # 연속되지 않으면 초기화
    return True

def solution(stones, k):
    left, right = 1, max(stones)
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        if can_cross(stones, k, mid):
            answer = mid
            left = mid +1
        else:
            right = mid - 1
    return answer
        