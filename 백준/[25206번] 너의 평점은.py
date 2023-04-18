d = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0,
     'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

tot_score = 0.0
tot_grade = 0.0
temp = 0.0
for _ in range(20):
    sub, score, grade = input().split()
    if grade == 'P':
        continue
    tot_score += float(score)
    
    temp += float(score) * float(d[grade])

print("{:.6f}".format(temp/tot_score))
