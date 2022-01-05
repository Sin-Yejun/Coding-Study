n = int(input())
x = []
for _ in range(n):
    w, h = map(int,input().split())
    x.append((w,h))
ranks=[]
for i in range(n):
    rank = 1
    for j in range(n):
        if i!=j:
            if x[i][0] < x[j][0] and x[i][1] < x[j][1]:
                rank+=1
    ranks.append(rank)
print(" ".join(map(str,ranks)))
            
        
