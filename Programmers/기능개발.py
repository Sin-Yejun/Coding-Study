def solution(progresses, speeds):
    func = []
    for i in range(len(progresses)):
        if (100-progresses[i]) % speeds[i] == 0:
            func.append((100-progresses[i]) // speeds[i])
        else:
            func.append((100-progresses[i]) // speeds[i] +1)
    cnt = 0
    Max = func[0]
    ans = []
    for i in func:
        if i > Max:
            Max = i
            ans.append(cnt)
            cnt = 1
        else:
            cnt += 1
    ans.append(cnt)
    return ans
