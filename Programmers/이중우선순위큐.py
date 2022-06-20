from collections import deque

def solution(operations):
    q = deque()
    for op in operations:
        op = op.split()
        if op[0] == 'I':
            q.append(int(op[1]))
        elif q and op[0] == 'D':
            if op[1] == '1':
                q.remove(max(q))
            elif op[1] == '-1':
                q.remove(min(q))
    if q:
        return [max(q), min(q)]
    else:
        return [0,0]
                
