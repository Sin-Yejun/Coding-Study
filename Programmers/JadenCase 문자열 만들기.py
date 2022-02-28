def solution(s):
    s = s.lower()
    arr = ''
    if s[0].isalpha():
        arr += s[0].upper()
    else:
        arr += s[0]
    if len(s)==1:
        return arr
    flag = False
    for i in range(1,len(s)):
        if s[i] == ' ':
            arr += s[i]
            flag = True
        elif flag == True:
            if s[i].isalpha():
                arr += s[i].upper()
            else:
                arr += s[i]
            flag = False
        elif flag == False:
            arr += s[i]
            flag = False
    return arr
