import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    command = list(sys.stdin.readline().split())
    if len(command) == 2:
        command[1] = int(command[1])
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack = stack[:len(stack)-1]
    
