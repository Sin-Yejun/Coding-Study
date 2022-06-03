from itertools import permutations
def solution(expression):
    op = []
    nums = []
    tmp = ''
    for i in expression:
        if i == '*' or i=='-' or i=='+':
            op.append(i)
            nums.append(int(tmp))
            tmp = ''
        else:
            tmp += i
    nums.append(int(tmp))
    set_op = list(set(op))
    Max = 0
    for per in permutations(set_op,len(set_op)):
        nums_copy = nums[:]
        op_copy = op[:]
        for i in per:
            for j in op:
                if i == j:
                    idx = op_copy.index(i)
                    op_copy.remove(i)
                    if i == '-':
                        tmp = nums_copy[idx] - nums_copy[idx+1]
                    elif i == '+':
                        tmp = nums_copy[idx] + nums_copy[idx+1]
                    else:
                        tmp = nums_copy[idx] * nums_copy[idx+1]
                    del nums_copy[idx]
                    del nums_copy[idx]
                    nums_copy.insert(idx,tmp)
        if len(nums_copy) == 2:
            if i == '-':
                tmp = nums_copy[0] - nums_copy[1]
            elif i == '+':
                tmp = nums_copy[0] + nums_copy[1]
            else:
                tmp = nums_copy[0] * nums_copy[1]
            Max = max(Max,abs(tmp))
        else:
            Max = max(Max,abs(nums_copy[0]))
    return Max
                
            
                
