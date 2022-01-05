total = 0
d = {}
for i in range(10):
    n = int(input())
    total+=n
    if n not in d:
        d[n]=0
    else:
        d[n]+=1
print(total//10)
rev_d = {key:val for val,key in d.items()}
print(rev_d[max(d.values())])
