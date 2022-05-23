def solution(n):
    answer = ''
    while n:
        if n % 3:   # 3의 배수가 아닐 때
            answer += str(n % 3)
            n //= 3
        else:       # 3의 배수 일 때
            answer += "4"
            n = n//3 - 1
    return answer[::-1]
