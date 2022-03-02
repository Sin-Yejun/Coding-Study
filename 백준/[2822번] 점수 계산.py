import sys
arr = []
index = []
for i in range(8):
    arr.append(int(sys.stdin.readline()))
total = 0
for i in range(5):
    total += max(arr)
    index.append(arr.index(max(arr)))
    arr[arr.index(max(arr))] = 0

print(total)
for i in sorted(index):
    print(i+1,end=' ')
