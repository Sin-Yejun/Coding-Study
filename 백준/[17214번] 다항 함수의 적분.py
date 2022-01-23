s = input()
flag = False
if s[0]=='-':
    s = s[1:]
    flag = True
l = []
for i in s:
    if i == '+':
        l.append(i)
    if i == '-':
        l.append(i)

s = s.replace('+',',').replace('-',',')
li = s.split(',')

sik = ''
cnt = 0
for i in li:
    temp = ''
    for j in i:
        if j!='x':
            temp += j
    
    if i.count('x') > 0:
        val = int(temp)//(i.count('x')+1)
        if val == 1:
            val = ''
        sik += str(val)+'x'*(i.count('x')+1)
    else:
        val = int(temp)
        if val == 1:
            val = ''
        sik += str(val)+'x'

    if cnt < len(l):
        sik += l[cnt]
        cnt += 1
    
        
sik += '+W'
if s == '0':
    sik = 'W'
if flag == True:
    sik = '-'+sik
print(sik)
    

