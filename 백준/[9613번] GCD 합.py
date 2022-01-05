def GCD(a,b):
    while b != 0:
        a, b = b, a%b
    return a
n = int(input())
for _ in range(n):
    arr = list(map(int,input().split()))
    del arr[0]
    s = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            s += GCD(arr[i], arr[j])
    print(s)

