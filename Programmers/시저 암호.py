def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper():
            temp = ord(i)+n
            if temp > 90:
                temp -= 26
            answer += chr(temp)
        elif i.islower():
            temp = ord(i)+n
            if temp > 122:
                temp -= 26
            answer += chr(temp)
        else:
            answer += ' '
    return answer
