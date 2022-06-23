import sys
input = sys.stdin.readline
n, m = map(int,input().split())
d = {}
for i in range(1,n+1):
    name = input().strip()
    d[str(i)] = name
    d[name] = i
problem = [input().strip() for i in range(m)]
for i in problem:
    print(d[i])
