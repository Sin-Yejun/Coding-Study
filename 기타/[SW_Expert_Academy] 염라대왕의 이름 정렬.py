T = int(input())

for i in range(T):
    arr = set()
    n = int(input())
    for j in range(n):
        arr.add(input())
    arr = list(arr)
    arr.sort(key = lambda x:(len(x),x))
    print('#%d'%(i+1))
    for k in arr:
        print(k)
