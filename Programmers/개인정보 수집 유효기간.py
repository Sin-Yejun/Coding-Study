from collections import defaultdict
def solution(today, terms, privacies):
    answer = []
    today_year = int(today[:4])
    today_month = int(today[5:7])
    today_day = int(today[8:10])
    d = defaultdict(int)
    for t in terms:
        N, T = t.split(' ')
        d[N] = int(T)
    cnt = 0
    for priv in privacies:
        flag = False
        cnt += 1
        D, typ = priv.split(' ')
        p_year = int(D[:4])
        p_month = int(D[5:7]) + d[typ]
        while p_month > 12:
            p_month -= 12
            p_year += 1
        p_day = int(D[8:10])
        #print(today, p_year,p_month,p_day)
        if today_year > p_year:
            answer.append(cnt)
        elif today_year == p_year:
            if today_month > p_month:
                answer.append(cnt)
            elif today_month == p_month:
                if today_day >= p_day:
                    answer.append(cnt)
    return answer
            
