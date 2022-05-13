def solution(n):
    answer = 0
    for i in range(1, 141): # 1 ~ 140까지 합이 9870으로 10000 미만의 수 중 가장 큰 수
        if n < i + sum(range(i)): break # n이 1 부터 i 개를 더한 값보다 작은 경우
        if (n-sum(range(i)))/i == int((n-sum(range(i)))/i): # 나누어 떨어짐 -> 패턴에 일치하는 경우
            answer += 1
    return answer
