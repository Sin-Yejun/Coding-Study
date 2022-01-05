import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

print(round(sum(arr)/len(arr)))
arr.sort()
print(arr[len(arr)//2])

dic = {}
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
b = []
for key, val in dic.items():
    if val == max(dic.values()):
        b.append(key)
if len(b)==1:
    print(b[0])
else:
    b.remove(min(b))
    print(min(b))
print(abs(max(arr)-min(arr)))
