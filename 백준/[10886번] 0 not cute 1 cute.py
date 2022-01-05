import sys
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

if arr.count(0) > arr.count(1):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')
