import sys
from collections import defaultdict
input = sys.stdin.readline
n, m = map(int, input().split())
d = defaultdict(str)
for _ in range(n):
    name, pw = input().split()
    d[name] = pw
for _ in range(m):
    print(d[input().strip()])
