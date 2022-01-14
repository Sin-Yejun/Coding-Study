# https://swoon1.tistory.com/3
def getscore(a):
    if s[i] == 'S':
        add = 10
        if frame < 10:
            plus.append(a+1)
            plus.append(a+2)
    elif s[a] == 'P':
        add = 10 - ad
        if frame < 10:
            plus.append(a+1)
    elif s[a] == '-':
        add = 0
    else:
        add = int(s[a])
    return add
 
s = list(input())
frame = 1
stack = 0
answer = 0
plus = []
 
for i in range(len(s)):
    ad = getscore(i)
    answer += ad*(plus.count(i)+1)
    stack += 1
    if (s[i] == 'S') | (stack == 2):
        stack = 0
        frame += 1
 
print(answer)
# 아래 내 코드는 반례를 못찾겠
'''
re = input()
score = 0
frame = 0
cnt = 0
for i in range(len(re)):
    frame = cnt//2 + 1
    if re[i].isdigit():
        score += int(re[i])
    if re[i] == 'P':
        if re[i-1] == '-':
            score += 10
        else:
            score += 10 - int(re[i-1])
        if frame < 10:
            if i+1 != len(re):
                if re[i+1].isdigit():
                    score += int(re[i+1])
                elif re[i+1] == 'S':
                    score += 10
    if re[i]=='S':
        score += 10
        cnt+=1
        if frame < 10:
            if i+1 != len(re):
                if i+2 != len(re) and re[i+2] == 'P':
                    if re[i+1] == '-':
                        score += 10
                    else:
                        score += 10 - int(re[i+1])
                if re[i+1].isdigit():
                    score += int(re[i+1])
                    if i+2 != len(re) and re[i+2].isdigit():
                        score += int(re[i+2])
                if re[i+1] == 'S':
                    score += 10
                    if i+2!=len(re) and re[i+2] == 'S':
                        score += 10
    cnt += 1
    print(re[i],score, frame)
print(score)
'''
