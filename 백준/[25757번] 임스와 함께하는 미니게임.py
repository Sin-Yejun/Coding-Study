import sys
input = sys.stdin.readline

n, y = input().split()
x = 0
if y == 'Y':
	x = 1
elif y == 'F':
	x = 2
else:
	x = 3
s = set()

for i in range(int(n)):
	name = input().strip()
	s.add(name)

print(len(s)//x)
