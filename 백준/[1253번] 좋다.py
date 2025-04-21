n = int(input())
arr = list(map(int, input().split()))
arr.sort()
good = 0
for i in range(n):
    target = arr[i]
    left, right = 0, n-1
    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
        temp = arr[left]+arr[right]
        if temp == target:
            good += 1
            break
        elif temp < target:
            left += 1
        else:
            right -= 1

print(good)