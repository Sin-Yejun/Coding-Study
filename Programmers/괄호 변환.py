def right(w):   # 올바른 괄호 문자열인지 확인
    stack = []
    for i in w:
        stack.append(i)
        if len(stack)>=2 and stack[-2] == '(' and stack[-1] == ')':
            stack = stack[:-2]      # stack의 끝에 2개가 '()' 이면 없애기
    if stack:       # stack에 남은 문자열 있다면 올바른 괄호 아님
        return False
    else:           # stack에 남은 문자열 없다면 올바른 괄호
        return True

def algorithm(w):
    if w == '':     # 1. 빈문자열인 경우, 빈 문자열 반환
        return ''
    g1 = 0          # '(' 개수
    g2 = 0          # ')' 개수
    for i in range(len(w)):     # 2. 균형잡힌 괄호 문자열 u, v 분리 과정
        if w[i] == '(':
            g1 += 1
        if w[i] == ')':
            g2 += 1
        if g1 == g2:    
            u = w[:i+1]
            v = w[i+1:]
            break
            
    if right(u):        # 3. u가 올바른 괄호 문자열이라면
        temp = u        # 3-1 내용 
        temp += algorithm(v)    
        return temp
    else:               # 4. u가 올바른 괄호 문자열이 아니라면
        temp = '('              # 4-1
        temp += algorithm(v)    # 4-2
        temp += ')'             # 4-3
        tmp = u[1:-1]           # 4-4
        for i in tmp:
            if i == '(':
                temp += ')'
            else:
                temp += '('
        return temp             # 4-5
    
def solution(p):
    return algorithm(p)
    
