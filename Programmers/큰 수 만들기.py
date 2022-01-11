# https://sanghyu.tistory.com/136
def solution(number, k):
    answer = ''
    stack = []
    for i in number:
        while stack and stack[-1] < i and k>0:
            k-=1
            stack.pop()
        stack.append(i)
    
    answer = "".join(stack[:len(stack)-k])
    return answer
