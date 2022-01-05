arr = []
for i in range(5):
    n = int(input())
    if n<40:
        n=40
    arr.append(n)

print(sum(arr)//5)
