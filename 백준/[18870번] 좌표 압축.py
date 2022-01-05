import sys

n = int(sys.stdin.readline())
arr = list(map(int,input().split()))
arr2 = sorted(list(set(arr)))

dic = {arr2[i] : i for i in range(len(arr2))}
for i in arr:
    print(dic[i],end=' ')




''' 시간초과 
n = int(input())
l = list(map(int,input().split()))
f = list(set(l))
f.sort()
t = []
idx = 0
for i in f:
    t.append((i,idx))
    idx+=1
ans = []
for i in l:
    for j in range(len(t)):
        if t[j][0] ==   i:
            ans.append(t[j][1])
print(' '.join(map(str,ans)))
'''
    
