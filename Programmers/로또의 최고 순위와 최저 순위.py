def solution(lottos, win_nums):
    zero = 0
    cnt = 0
    for i in lottos:
        if i == 0:
            zero += 1
        if i in win_nums:
            cnt += 1
    high = zero + cnt
    low = cnt
    dic = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    return[dic[high], dic[low]]
