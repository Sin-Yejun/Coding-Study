from bisect import bisect_left, bisect_right
def get_subarray_sums(arr):
    n = len(arr)
    sub_sums = []
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += arr[j]
            sub_sums.append(total)
    return sub_sums

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))


sumA = get_subarray_sums(A)
sumB = get_subarray_sums(B)

sumA.sort()
count = 0
for b in sumB:
    target = T - b 
    left = bisect_left(sumA, target)
    right = bisect_right(sumA, target)
    count += right-left

print(count)