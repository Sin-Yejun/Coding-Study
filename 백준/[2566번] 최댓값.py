row = 1
col = 1
Max = 0
for i in range(9):
    arr = list(map(int, input().split()))
    if max(arr) > Max:
        Max = max(arr)
        row = i+1
        col = arr.index(Max)+1

print(Max)
print(row, col)
