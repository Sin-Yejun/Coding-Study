import sys
input = sys.stdin.readline
n, m = map(int,input().split())
big_set = []
sub_set = []
for _ in range(n):
    big_set.append(input().strip())
for _ in range(m):
    sub_set.append(input().strip())
cnt = 0
for i in sub_set:
    if i in big_set:
        cnt += 1
print(cnt)
