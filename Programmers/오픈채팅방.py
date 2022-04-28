def solution(record):
    dict_id = {}
    result = []
    seq = []
    for i in record:
        line = i.split()
        if line[0] == 'Enter':
            dict_id[line[1]] = line[2]
            seq.append(['Enter',line[1]])
        elif line[0] == 'Leave':
            seq.append(['Leave', line[1]])
        elif line[0] == 'Change':
            dict_id[line[1]] = line[2]
    ans = []
    for i in range(len(seq)):
        if seq[i][0] == 'Enter':
            ans.append(dict_id[seq[i][1]]+'님이 들어왔습니다.')
        else:
            ans.append(dict_id[seq[i][1]]+'님이 나갔습니다.')
    return ans
