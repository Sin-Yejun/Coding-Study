def solution(n):
    three = ''
    while n > 0:
        n, r = divmod(n,3)
        three += str(r)
    return int(three,3)
