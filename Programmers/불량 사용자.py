from collections import defaultdict
from itertools import permutations
def check(user, ban):
    if len(ban) == len(user):
        for k in range(len(ban)):
            if ban[k] == '*':
                continue
            if ban[k] != user[k]:
                return False
        return True
    else:
        return False
                
                        
def solution(user_id, banned_id):
    result = set()

    for perm in permutations(user_id, len(banned_id)):
        if all(check(u, b) for u, b in zip(perm, banned_id)):
            result.add(frozenset(perm))  # 순서 상관없게 하기 위해 frozenset 사용

    return len(result)
                