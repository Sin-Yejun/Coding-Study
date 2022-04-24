# https://velog.io/@syhan28/2022-KAKAO-%EA%B3%B5%EC%B1%84-%EC%8B%A0%EA%B3%A0-%EA%B2%B0%EA%B3%BC-%EB%B0%9B%EA%B8%B0%ED%8C%8C%EC%9D%B4%EC%8D%AC
from collections import defaultdict
def solution(id_list, report, k):
    dic_name = defaultdict(set)
    dic = defaultdict(int)
    report = set(report)
    arr = []
    for i in report:
        a, b = i.split()
        dic[b] += 1
        dic_name[a].add(b)
        if dic[b] == k:
            arr.append(b)
    ans = [0] * len(id_list)
    for i in arr:
        for j in range(len(id_list)):
            if i in dic_name[id_list[j]]:
                ans[j] += 1
    return ans
    
            
