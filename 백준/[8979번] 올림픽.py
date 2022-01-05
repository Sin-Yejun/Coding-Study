n, k = map(int, input().split())
total = []
for _ in range(n):
    contry = list(map(int,input().split()))
    total.append(contry)
total.sort(key = lambda x : (x[1],x[2],x[3]), reverse=True)
grade, s = 1, 0
for i in range(n):
    if i !=0:
        if total[i-1][1:] == total[i][1:]:
            s += 1
        else:
            if s:
                grade += s
                s = 0
            grade += 1
    if total[i][0] == k:
        print(grade)
        break
    
