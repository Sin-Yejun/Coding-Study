def solution(a, b):
    answer = 0
    m = min(a,b)
    M = max(a,b)
    if m==M:
        return m
    else:
        for i in range(m,M+1):
            answer += i
        return answer
