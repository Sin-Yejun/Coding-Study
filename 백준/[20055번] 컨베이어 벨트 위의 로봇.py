from collections import deque
n, k = map(int, input().split())
arr = deque(list(map(int, input().split())))
robots = deque([0 for _ in range(n)])

answer = 0
checkzero = sum([1 for i in arr if i == 0])

while checkzero < k:

    # 1. 시계 방향으로 회전
    arr.rotate(1) 
    robots.rotate(1)
    if robots[-1] == 1: # 언제든 로봇 끝에 도착하면 내리기
        robots[-1] = 0

    # 2. 로봇 이동
    for i in range(len(robots)-2, -1, -1):
        if robots[i] == 1 and robots[i+1] != 1 and arr[i+1] > 0:
            robots[i], robots[i+1] = robots[i+1], robots[i]
            arr[i+1] -= 1
    if robots[-1] == 1: # 언제든 로봇 끝에 도착하면 내리기
        robots[-1] = 0

    # 3. 로봇 올리기
    if arr[0] > 0:
        robots[0] = 1
        arr[0] -= 1

    # 4. 내구도 체크
    checkzero = sum([1 for i in arr if i == 0])
    answer += 1
    
print(answer)