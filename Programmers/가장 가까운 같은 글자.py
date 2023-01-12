from collections import defaultdict
def solution(s):
    answer = []
    d = defaultdict(int)
    idx = 0
    for i in s:
        if i not in d:
            answer.append(-1)
            d[i] = idx
        else:
            answer.append(idx - d[i])
            d[i] = idx
        idx += 1
    return answer
            
