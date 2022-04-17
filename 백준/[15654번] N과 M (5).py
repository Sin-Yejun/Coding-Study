# https://jjyoung.tistory.com/79
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
                stack.append(i)
                back_tracking()
                stack.pop()

back_tracking()
