import sys

# 수식의 길이 입력
n = int(sys.stdin.readline())

# 수식 문자열 입력
exp = sys.stdin.readline().strip()

# 숫자와 연산자를 각각 리스트에 분리
nums = []  # 숫자들 저장
ops = []   # 연산자들 저장

for i in range(n):
    if i % 2 == 0:  # 짝수 인덱스는 숫자
        nums.append(int(exp[i]))
    else:           # 홀수 인덱스는 연산자
        ops.append(exp[i])

# 최댓값을 저장할 변수 (초기값은 매우 작은 값)
max_result = -float('inf')

# 연산을 실제로 수행하는 함수
def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:  # '*'
        return a * b

# DFS로 괄호를 넣는 모든 경우 탐색
def dfs(index, current_result):
    global max_result

    # 마지막 연산자까지 도달한 경우, 결과 갱신
    if index >= len(ops):
        max_result = max(max_result, current_result)
        return

    # 1. 괄호 없이 계산하는 경우
    next_result = calc(current_result, nums[index + 1], ops[index])
    dfs(index + 1, next_result)

    # 2. 괄호를 사용하는 경우 (다음 연산자까지 고려해서 괄호로 묶음)
    if index + 1 < len(ops):
        # 먼저 괄호 안 계산을 해두고
        bracket = calc(nums[index + 1], nums[index + 2], ops[index + 1])
        # 그 결과를 현재 값과 다시 계산
        new_result = calc(current_result, bracket, ops[index])
        # 다음 index는 2칸 건너뛰기 (괄호 친 부분 건너뜀)
        dfs(index + 2, new_result)

# DFS 탐색 시작 (처음 숫자부터 시작)
dfs(0, nums[0])

# 최종 결과 출력
print(max_result)
