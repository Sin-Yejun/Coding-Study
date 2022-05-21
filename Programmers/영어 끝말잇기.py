def solution(n, words):
    word_dict = {}
    cnt = -1
    for i in range(len(words)):
        if i!= 0 and words[i-1][-1] != words[i][0]:
            cnt = i
            break
        if words[i] in word_dict:
            cnt = i
            break
        else:
            word_dict[words[i]] = 1
    if cnt == -1:
        return [0,0]
    return [cnt%n+1, cnt//n+1]
