T = int(input())
for a in range(T):
    n = int(input())
    arr = []
    for b in range(n):
        x, y = input().split()
        y = int(y)
        arr.append([x,y])
    arr.sort(key =lambda x:-x[1])
    print(arr[0][0])
        
