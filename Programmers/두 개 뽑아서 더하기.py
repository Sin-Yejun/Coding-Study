from itertools import combinations
def solution(numbers):
    comb = list(combinations(numbers,2))
    result = []
    for a, b in comb:
        result.append(a+b)
    result = list(set(result))
    result.sort()
    return result
