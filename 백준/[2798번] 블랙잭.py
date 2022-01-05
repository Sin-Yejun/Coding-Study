n, m = map(int,input().split())
l = list(map(int,input().split()))
s = []
flag = True
for i in range(len(l)-2):
    for j in range(i+1,len(l)-1):
        for k in range(j+1,len(l)):
            if l[i]+l[j]+l[k] == m:
                print(m)
                flag = False
                break
            elif l[i]+l[j]+l[k] < m:
                s.append(l[i]+l[j]+l[k])
        if flag==False:
            break
    if flag==False:
        break
            
if flag == True:    
    print(max(s))
                
