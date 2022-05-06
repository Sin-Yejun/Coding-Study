def solution(s):
    if s[0] == '+':
        return int(s[1:])
    elif s[0] == '-':
        return -int(s[1:])
    else:
        return int(s)
