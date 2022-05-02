def solution(s):
    arr = list(s)
    arr.sort(reverse=True)
    return ''.join(arr)
