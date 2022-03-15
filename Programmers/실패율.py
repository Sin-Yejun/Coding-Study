# https://it-garden.tistory.com/235
def solution(N, stages):
    result = {}
    d = len(stages)
    for i in range(1, N+1):
        if d != 0:
            cnt = stages.count(i)
            result[i] = cnt / d
            d -= cnt
        else:
            result[i] = 0
    return sorted(result, key = lambda x : result[x], reverse = True)
