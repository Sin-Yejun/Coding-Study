s = 0
arr = []
for _ in range(4):
    a, b = map(int,input().split())
    s -= a
    s += b
    arr.append(s)
print(max(arr))
