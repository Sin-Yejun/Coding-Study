def solution(s):
    answer = True
    s = s.lower()
    p = 0
    y = 0
    for i in s:
        if i == 'y':
            y +=1
        if i == 'p':
            p +=1
    if y==p:
        return True
    else:
        return False
