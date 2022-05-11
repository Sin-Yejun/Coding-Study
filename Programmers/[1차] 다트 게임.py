def solution(dartResult):
    arr = []
    num = ''
    for i in dartResult:
        if i.isdigit():
            num += i
        else:
            if num:
                arr.append(int(num))
            num = ''
        if i == 'D':
            arr[-1] = arr[-1]**2
        elif i == 'T':
            arr[-1] = arr[-1]**3
        elif i == '*':
            if len(arr) == 1:
                arr[-1] *= 2
            else:
                arr[-1] *= 2
                arr[-2] *= 2
        elif i == '#':
            arr[-1] = -arr[-1]
    return sum(arr)
