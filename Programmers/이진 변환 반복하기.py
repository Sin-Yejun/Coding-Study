def solution(s):
    zero = 0
    cnt = 0
    c = s
    while True:
        zero += c.count('0')
        cnt += 1
        c = c.count('1')
        if c == 1:
            break
        c = str(bin(c)[2:])
    return [cnt, zero]
