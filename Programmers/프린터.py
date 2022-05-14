def solution(priorities, location):
    answer = [0 for i in range(len(priorities))]
    idx = 0
    cnt = 0
    while answer.count(0) != 0:
        if idx == len(priorities):
            idx = 0
        if max(priorities) == priorities[idx]:
            cnt += 1
            priorities[idx] = 0
            answer[idx] = cnt
        idx += 1
    return answer[location]
        
