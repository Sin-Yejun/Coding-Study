from string import ascii_uppercase
def solution(msg):
    alpha_dict = {}
    for idx, i in enumerate(ascii_uppercase):
        alpha_dict[i] = idx+1
    answer = []
    
    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(alpha_dict[msg[w:c]])
            break
        if msg[w:c+1] not in alpha_dict:
            alpha_dict[msg[w:c+1]] = len(alpha_dict) + 1
            answer.append(alpha_dict[msg[w:c]])
            w = c

    return answer
            
    
