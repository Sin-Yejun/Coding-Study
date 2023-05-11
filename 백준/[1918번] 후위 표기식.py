s = input()
p = {'+':2, '-':2, '*':3, '/':3, '(':1}
stack = []
postfix_expression = []

for i in s:
    if i.isalpha():
        postfix_expression.append(i)
    elif i == '(':
        stack.append(i)
    elif i == ')':
        x = stack.pop()
        while x != '(':
            postfix_expression.append(x)
            x = stack.pop()
    else:
        while (len(stack) != 0) and (p[stack[-1]] >= p[i]):
            postfix_expression.append(stack.pop())
        stack.append(i)
while stack:
    postfix_expression.append(stack.pop())

print(''.join(postfix_expression))
        
