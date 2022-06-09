# https://velog.io/@hannahf97/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-n2-%EB%B0%B0%EC%97%B4-%EC%9E%90%EB%A5%B4%EA%B8%B0
def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        a = i//n # 몫
        b = i%n #나머지 
        if a<b: 
            a,b = b,a
        answer.append(a+1)
    
    return answer
