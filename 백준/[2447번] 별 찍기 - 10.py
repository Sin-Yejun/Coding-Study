# https://cotak.tistory.com/38
def draw(n):
    if n == 1:
        return ['*']

    star = draw(n//3)
    l = []
    for s in star:
        l.append(s*3)
    for s in star:
        l.append(s+' '*(n//3)+s)
    for s in star:
        l.append(s*3)
    return l

n = int(input())
print('\n'.join(draw(n)))
    
