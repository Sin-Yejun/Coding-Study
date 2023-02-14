def solution(input_string):
    arr = []
    answer = ''
    for i in input_string:
        if i in arr:
            if arr[-1] != i:
                answer += i
        arr.append(i)
    answer = ''.join(set(answer))
    answer = sorted(answer)
    if answer:
        return ''.join(answer)
    else:
        return 'N'