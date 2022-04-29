def solution(sizes):
    l1 = []
    l2 = []
    for a,b in sizes:
        M = max(a,b)
        m = min(a,b)
        l1.append(M)
        l2.append(m)
    return max(l1)*max(l2)
