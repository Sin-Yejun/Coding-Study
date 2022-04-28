from collections import deque
stack = deque()
def solution(s):
    for i in s:
        if not stack:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
        elif stack[-1] != i:
            stack.append(i)
    if stack:
        return 0
    else:
        return 1
            
        
