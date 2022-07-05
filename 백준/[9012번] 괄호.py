import sys
input = sys.stdin.readline
def check(string):
    stack = []
    for i in string:
        stack.append(i)
        if len(stack) >= 2 and stack[-2] == '(' and stack[-1] == ')':
            stack = stack[:-2]
    if stack:
        return False
    else:
        return True
            
n = int(input())
for i in range(n):
    string = input().strip()
    if check(string):
        print('YES')
    else:
        print('NO')
