import sys
input = sys.stdin.readline
n = int(input())
sang = list(map(int,input().split()))
m = int(input())
num = list(map(int,input().split()))

sang.sort()

def binary_search(left, right, array, target):
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None

for i in num:
    if binary_search(0, n-1, sang, i) is not None:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
