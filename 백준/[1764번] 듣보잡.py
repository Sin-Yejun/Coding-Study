# https://wook-2124.tistory.com/476
import sys

N, M = map(int,input().split())
no1 = set()
no2 = set()
for _ in range(N):
    no1.add(sys.stdin.readline().strip())

for _ in range(M):
    no2.add(sys.stdin.readline().strip())

ans = sorted(list(no1 & no2))


print(len(ans))
for i in ans:
    print(i)
