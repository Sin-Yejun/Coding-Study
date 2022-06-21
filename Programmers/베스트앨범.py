def solution(genres, plays):
    N = len(genres)
    d = {}
    for i in range(N):
        g = genres[i]
        if g in d:
            d[g][i] = plays[i]
        else:
            d[g] = {i:plays[i]}
    d = dict(sorted(d.items(), key = lambda x:-sum(x[1].values())))
    answer = []
    for key, val_dic in d.items():
        val_dic = sorted(val_dic.items(), key= lambda x:-x[1])[:2]
        for key, val in val_dic:
            answer.append(key)
    return answer
