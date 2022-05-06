def solution(n):
    subak = ''
    for i in range(n):
        if i%2==1:
            subak += '박'
        else:
            subak += '수'
    return subak
