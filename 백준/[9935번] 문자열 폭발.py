s = input()
r = list(input())
L = len(r)
stack = []
for i in s:
    stack.append(i)
    if stack[-1] == r[-1]:
        if stack[-L:] == r:
            for _ in range(L):
                stack.pop()
if not stack:
    print('FRULA')
else:
    print(''.join(stack))


