import sys
from itertools import combinations
input = sys.stdin.readline
while True:
    arr = list(map(int,input().split()))
    if arr == [0]:
        break
    k = arr[0]
    arr = arr[1:]
    for arr in list(combinations(arr,6)):
        print(*arr)
    print()
    
