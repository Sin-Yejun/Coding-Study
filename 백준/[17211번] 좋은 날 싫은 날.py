n , f = map(int,input().split())
mood = list(map(float, input().split()))
pos = [0 for i in range(n)]
neg = [0 for i in range(n)]
if f==0:
    pos[0] = mood[0]
    neg[0] = mood[1]
else:
    pos[0] = mood[2]
    neg[0] = mood[3]

for i in range(1,n):
    pos[i] = pos[i-1] * mood[0] + neg[i-1] * mood[2]
    neg[i] = pos[i-1] * mood[1] + neg[i-1] * mood[3]
    
print(round(pos[n-1]*1000))
print(round(neg[n-1]*1000))

    


