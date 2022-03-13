while True:
    stack = []
    flag = True
    s = input()
    if s == ".": break
    for c in s:
        if c == "(":
            stack.append(c)
        elif c == "[":
            stack.append(c)
        elif c == ")":
            if len(stack) == 0:
                flag = False
                break
            if stack[-1] == "(":
                stack = stack[:-1]
            else:
                flag = False
                break
        elif c == "]":
            if len(stack) == 0:
                flag = False
                break
            if stack[-1] == "[":
                stack = stack[:-1]
            else:
                flag = False
                break
    if len(stack) == 0 and flag == True:
        print("yes")
    else:
        print("no")
        
            
