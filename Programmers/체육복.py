def solution(n, lost, reserve):
    answer = n - len(lost)
    lost.sort()
    reserve.sort()
    idx = 0
    temp = []
    for i in reserve:
        if i in lost:
            answer += 1
            temp.append(i)
    while temp:
        x = temp.pop()
        lost.remove(x)
        reserve.remove(x)
    idx = 0
    for i in lost:
        for j in reserve[idx:]:
            if i == j-1:
                answer += 1
                idx += 1
                break
            elif i == j+1:
                answer += 1
                idx += 1
                break
    return answer
