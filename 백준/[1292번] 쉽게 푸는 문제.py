a, b = map(int,input().split())
arr = []
index = 1
while len(arr)<b:
    for _ in range(index):
        arr.append(index)
    index += 1
print(sum(arr[a-1:b]))
    
