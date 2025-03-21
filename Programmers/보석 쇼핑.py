from collections import defaultdict
def solution(gems):
    kinds = len(set(gems))
    jewel = defaultdict(int)
    left = 0
    answer = [0, len(gems)-1]
    
    for right in range(len(gems)):
        jewel[gems[right]] += 1
        
        while kinds == len(jewel):
            
            if answer[1]-answer[0] > right - left:
                answer = [left, right]
                
            jewel[gems[left]] -= 1
            if jewel[gems[left]] == 0:
                del jewel[gems[left]]
            left += 1
    return [answer[0] + 1, answer[1] + 1]