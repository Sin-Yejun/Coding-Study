def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = ''
        a = bin(arr1[i])[2:]
        b = bin(arr2[i])[2:]
        #print(a,b)
        while len(a) != n:
            a = '0'+a
        while len(b) != n:
            b = '0'+b
        for j in range(n):
            #print(a[j], b[j])
            if a[j] == '1' or b[j] == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
    return answer
        
        
