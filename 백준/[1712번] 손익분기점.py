a,b,c=map(int,input().split())
margin= c-b
if margin>0:
    n = a//margin
    n+=1
    print(n)
else:
    print(-1)

  
