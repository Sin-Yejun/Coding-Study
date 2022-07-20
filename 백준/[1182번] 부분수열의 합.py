from itertools import combinations
n, s = map(int,input().split())
arr = list(map(int, input().split()))
answer = 0
for i in range(1, n+1):
    for com in combinations(arr, i):
        if sum(com) == s:
            answer += 1

print(answer)
