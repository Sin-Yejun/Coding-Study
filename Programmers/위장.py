def solution(clothes):
    dic = {}
    for name, kinds in clothes:
        if kinds not in dic:
            dic[kinds] = 1
        else:
            dic[kinds] += 1
    tmp = 1
    
    for key, val in dic.items():
        tmp *= (val+1)
        
    return tmp -1
        
        
