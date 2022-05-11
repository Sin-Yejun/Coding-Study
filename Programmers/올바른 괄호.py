def solution(s):
    arr = []
    for i in s:
        arr.append(i)
        if len(arr) > 1:
            if arr[-2] == '(' and arr[-1] == ')':
                arr.pop()
                arr.pop()
    if arr:
        return False
    else:
        return True
            
