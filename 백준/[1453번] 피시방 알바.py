n = int(input())
arr = list(map(int,input().split()))
arr2 = []
cnt = 0
for i in arr:
    if i not in arr2:
        arr2.append(i)
    else:
        cnt+=1
print(cnt)
