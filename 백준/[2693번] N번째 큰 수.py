import sys
inp = sys.stdin.readline

n = int(inp())
for _ in range(n):
    arr = list(map(int,inp().split()))
    arr.remove(max(arr))
    arr.remove(max(arr))
    print(max(arr))
