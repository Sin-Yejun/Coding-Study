def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

for x in arr2:
    result = binary_search(arr1, x, 0, n-1)
    if result:
        print('yes', end = ' ')
    else:
        print('no', end=' ')
