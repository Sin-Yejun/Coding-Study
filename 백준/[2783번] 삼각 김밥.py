import sys
inf = sys.stdin
ouf = sys.stdout
li = []
X, Y = map(float, inf.readline().split())
li.append(X/Y*1000)

n = int(inf.readline())
for _ in range(n):
    x, y = map(float, inf.readline().split())
    li.append(x/y*1000)

ouf.write("{:.2f}".format(min(li)))

