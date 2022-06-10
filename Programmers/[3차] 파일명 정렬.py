def solution(files):
    arr = []
    for file in files:
        Head = ''
        for i in range(len(file)):
            if not '0' <= file[i] <= '9':
                Head += file[i]
            else:
                break
        Number = ''
        for j in range(i, len(file)):
            if '0' <= file[j] <= '9':
                Number += file[j]
            else:
                break
        if j == len(file)-1:
            Tail = ''
        else:
            Tail = file[j:len(file)]
        arr.append([Head,Number,Tail])
    arr.sort(key = lambda x:[x[0].upper(),int(x[1])])
    return [''.join(i) for i in arr]
