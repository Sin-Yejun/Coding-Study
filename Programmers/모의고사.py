def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    if len(answers) > len(p1):
        p1 = p1*(len(answers)//len(p1)+1)
    if len(answers) > len(p2):
        p2 = p2*(len(answers)//len(p2)+1)
    if len(answers) > len(p3):
        p3 = p3*(len(answers)//len(p3)+1)
    s = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == p1[i]:
            s[0] += 1
        if answers[i] == p2[i]:
            s[1] += 1
        if answers[i] == p3[i]:
            s[2] += 1
    Max = max(s)
    ans = []
    for i in range(3):
        if s[i] == Max:
            ans.append(i+1)
    return ans
