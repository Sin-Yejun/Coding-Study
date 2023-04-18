arr = []
Max = 0
for _ in range(5):
    temp = list(map(str,input()))
    arr.append(temp)
    Max = max(len(temp),Max)
for i in range(5):
    if len(arr[i]) < Max:
        for _ in range(Max-len(arr[i])):
            arr[i].append('')

for k in zip(*arr):
    print(''.join(k),end='')
