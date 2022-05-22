from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    info_dict = {}
    for i in range(len(info)):
        temp = info[i].split()
        key = temp[:-1]
        val = int(temp[-1])
        for j in range(5):
            for com in combinations(key,j):
                tmp = ''.join(com)
                if tmp in info_dict:
                    info_dict[tmp].append(val)
                else:
                    info_dict[tmp] = [val]
    for k in info_dict:
        info_dict[k].sort()
    
    for q in query:
        temp = q.split(' ')
        q_key = temp[:-1]
        q_val = temp[-1]

        while 'and' in q_key:
            q_key.remove('and')
        while '-' in q_key:
            q_key.remove('-')
        q_key = ''.join(q_key) 

        if q_key in info_dict:
            scores = info_dict[q_key]

            if scores:
                enter = bisect_left(scores, int(q_val))
                answer.append(len(scores) - enter)
        else:
            answer.append(0)
    #print(info_dict)
    return answer
