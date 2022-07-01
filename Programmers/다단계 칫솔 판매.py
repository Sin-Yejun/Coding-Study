from collections import defaultdict
def solution(enroll, referral, seller, amount):
    d = defaultdict(list)
    for i in range(len(enroll)):
        if referral[i] == '-':
            d[enroll[i]].append('center')
        else:
            d[enroll[i]].append(referral[i])
        d[enroll[i]].append(0)
    
    
    for i in range(len(seller)):
        val = amount[i]*100
        name = seller[i]
        if val == 0:
            continue
        while name != 'center':
            new_val = val * 0.1
            new_val = int(new_val)
            val = val - new_val
            d[name][1] += int(val)
            name = d[name][0]
            val = new_val
            if int(val) <= 0:
                break
    answer = []
    for name, val in d.values():
        answer.append(round(val))
    return answer
