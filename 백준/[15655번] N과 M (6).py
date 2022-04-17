n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
stack = []

def back_tracking():
    if len(stack) == m:
        print(' '.join(map(str,stack)))
    else:
        for i in arr:
            if i not in stack:
                if stack and stack[-1] > i:
                    continue
                stack.append(i)
                back_tracking()
                stack.pop()
            

back_tracking()
