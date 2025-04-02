import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
arr = list(input().strip() for _ in range(n))
d = defaultdict(int)
#print()
for s in arr:
    string = s.split(' ')
    #print(string)
    # 첫 글자 단축키 지정 성공시
    succes = False
    break_flag = False
    check_alpha = ''
    answer = ''
    once = 0
    cnt = 0
    #print(s)
    for i in string:
        #print(i)
        if i[0] not in d and (chr(ord(i[0]) - 32) not in d and chr(ord(i[0]) + 32) not in d):
            d[i[0]] = 1
            #print(i[0])
            check_alpha = i[0]
            succes = True
            break_flag = True
            break
        if break_flag:
            break
    #print()
    #print()
    if check_alpha:
        for i in string:
            cnt += 1
            if i[0] == check_alpha and once == 0:
                once = 1
                answer += f'[{i[0]}]{i[1:]}'
            else:
                if cnt != 1:
                    answer += ' '
                answer += i
        print(answer)
    if succes:
        continue
    # 첫 글자 단축키 지정 실패시
    for k in s:
        if k != ' ' and (chr(ord(k) - 32) not in d and chr(ord(k) + 32) not in d) and k not in d:
            d[k] = 1
            #print(k)
            check_alpha = k
            break
    if check_alpha:
        for i in s:
            if i == check_alpha and once == 0:
                once = 1
                answer += f'[{i}]'
            else:
                answer += i
        print(answer)
    else:
        print(s)
