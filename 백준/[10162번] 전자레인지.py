t = int(input())
bt = [300,60,10]
arr = [0,0,0]

for i in range(3):
    if t >= bt[i]:
        arr[i] = t//bt[i]
        t -= t//bt[i] * bt[i]

if t == 0:
    print(' '.join(map(str, arr)))
else:
    print(-1)
