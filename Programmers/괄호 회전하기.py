from collections import deque
def check(s):
    stack = []
    for i in s:
        stack.append(i)
        #print(stack)
        if len(stack) > 1:
            if stack[-1] == ']' and stack[-2] == '[':
                stack = stack[:-2]
            elif stack[-1] == ')' and stack[-2] == '(':
                stack = stack[:-2]
            elif stack[-1] == '}' and stack[-2] == '{':
                stack = stack[:-2]
    if stack:
        return False
    else:
        return True
def solution(s):
    n = len(s)
    arr = deque(list(s))
    answer = 0
    for i in range(n):
        arr.rotate(-1)
        if check(arr):
            answer += 1
    return answer
