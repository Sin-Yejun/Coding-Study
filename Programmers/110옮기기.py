def solution(s):
    answer = []
    for string in s:
        stack = []
        count_110 = 0
        
        # 스택을 활용하여 "110" 제거 및 개수 세기
        for char in string:
            stack.append(char)
            if len(stack) >= 3 and stack[-3:] == ['1', '1', '0']:
                stack.pop()
                stack.pop()
                stack.pop()
                count_110 += 1
        
        # 남은 문자열에서 '0'의 위치 찾기
        idx = -1
        for i in range(len(stack)):
            if stack[i] == '0':
                idx = i
        
        # "110"을 삽입하여 새로운 문자열 생성
        if idx == -1:
            # '0'이 없는 경우
            result = '110' * count_110 + ''.join(stack)
        else:
            # '0'이 있는 경우
            result = ''.join(stack[:idx+1]) + '110' * count_110 + ''.join(stack[idx+1:])
        
        answer.append(result)
    
    return answer
