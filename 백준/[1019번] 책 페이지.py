n = int(input())
count = 0
i = 1
count = [0]*10
while i <= n:
    left = n // (i*10)
    cur = (n//i) % 10
    right = n%i
    for d in range(10):
        if d == 0:
            if left == 0:
                continue
            count[d] -= i

        if cur > d:
            count[d] += (left + 1) * i
        elif cur == d:
            count[d] += left * i + (right + 1)
        else:
            count[d] += left * i
    i*=10
print(" ".join(map(str,count)))