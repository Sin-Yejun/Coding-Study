def solution(absolutes, signs):
    ans = 0
    for i in range(len(signs)):
        if signs[i]:
            ans += absolutes[i]
        else:
            ans -= absolutes[i]
    return ans
