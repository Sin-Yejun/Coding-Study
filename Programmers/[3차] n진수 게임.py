def N_notation_cal(n,t,m):
    arr = []
    for i in range(t*m+1):
        temp = []
        while i != 0:
            r = i % n
            i = i // n
            if r >= 10:
                temp.append(chr(r+55))
            else:
                temp.append(r)
        arr.extend(temp[::-1])
    return [0]+arr
def solution(n, t, m, p):
    arr = N_notation_cal(n,t,m)
    answer = ''
    for i in range(p-1, len(arr), m):
        answer += str(arr[i])
    return answer[:t]
