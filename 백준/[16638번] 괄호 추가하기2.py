import sys
import copy

# 입력
n = int(sys.stdin.readline())
exp = list(sys.stdin.readline().strip())

max_result = -float('inf')

# 연산 수행 함수
def calc(a, b, op):
    a, b = int(a), int(b)
    if op == '+':
        return str(a + b)
    elif op == '-':
        return str(a - b)
    elif op == '*':
        return str(a * b)

# 수식 평가 함수 (우선순위에 따라 연산)
def evaluate(expr):
    expr = copy.deepcopy(expr)
    
    # 1. * 먼저 처리
    i = 0
    while i < len(expr):
        if expr[i] == '*':
            result = calc(expr[i-1], expr[i+1], '*')
            # prev op next 를 result로 대체
            expr[i-1:i+2] = [result]
            i -= 1  # 리스트 줄었으니 한 칸 앞에서 다시 시작
        else:
            i += 1

    # 2. 그다음 +, - 왼쪽부터 처리
    i = 0
    while len(expr) > 1:
        result = calc(expr[0], expr[2], expr[1])
        expr[0:3] = [result]
    return int(expr[0])

# DFS로 괄호 조합 시도
def dfs(index, expr):
    global max_result

    if index >= len(expr):
        max_result = max(max_result, evaluate(expr))
        return

    # 1. 괄호 안 치고 다음 연산자로 이동
    dfs(index + 2, expr)

    # 2. 괄호 치는 경우: (숫자 op 숫자) → 계산해서 넣기
    if index + 2 < len(expr):
        # 괄호로 묶을 부분 계산
        result = calc(expr[index], expr[index + 2], expr[index + 1])
        # 새로운 수식 구성
        new_expr = expr[:index] + [result] + expr[index + 3:]
        dfs(index + 2, new_expr)  # 다음 연산자 위치로 이동 (중첩 방지)

# DFS 시작
dfs(0, exp)

# 결과 출력
print(max_result)
