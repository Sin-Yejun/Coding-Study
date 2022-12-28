def solution(A, B):
    A.sort(reverse = True)
    B.sort(reverse = True)
    score = 0
    
    for a in A:
        if a >= B[0]:
            continue
        else:
            score += 1
            del B[0]
    return score