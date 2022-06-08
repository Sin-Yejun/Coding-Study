def measure(n):
    if n == 1:
        return 0
    arr = []
    for i in range(2, int(n**0.5)+1):
        if n // i > 10** 7:
            continue
        if n % i == 0:
            return n//i
    return 1
        
def solution(begin, end):
    return [measure(i) for i in range(begin, end+1)]
