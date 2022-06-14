def conversion(n, k):   # n을 k 진수로 변환
    arr = []
    while n!= 0:
        r = n%k
        n = n//k
        arr.append(r)
    return ''.join(list(map(str,arr[::-1])))

def prime_check(n):     # n이 소수인지 아닌지 판별
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def solution(n, k):
    con = conversion(n,k)
    arr = con.split('0')    # 0을 기준으로 나눠줌
    answer = 0
    for num in arr:
        if num and prime_check(int(num)):
            answer += 1
    return answer
