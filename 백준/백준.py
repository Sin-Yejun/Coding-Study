a,b=map(int,input().split())
list1=[]
for i in range(a,b+1):
    ct=0
    for j in range(1,i+1):
        if i%j==0:
            ct+=1
            if ct>2:
                break
        j=j*j
    if ct==2:
       print(i)
       
        
        
