x, y, w, h = map(int,input().split())

a = min(abs(x), abs(x-w))
b = min(abs(y), abs(y-h))
print(min(a,b))
