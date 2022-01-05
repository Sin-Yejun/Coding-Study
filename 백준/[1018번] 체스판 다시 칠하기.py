# https://leejunggae.tistory.com/14
n, m = map(int,input().split())
l = []
mini=[]
for _ in range(n):
    l.append(input())

for i in range(n-7):
    for j in range(m-7):
        idx1 = 0
        idx2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if(a+b)%2==0:
                    if l[a][b] != 'W':
                        idx1 += 1
                    if l[a][b] != 'B':
                        idx2 += 1
                else:
                    if l[a][b] != 'B':
                        idx1 +=1
                    if l[a][b] != 'W':
                        idx2 +=1
        mini.append(idx1)
        mini.append(idx2)
print(mini)
