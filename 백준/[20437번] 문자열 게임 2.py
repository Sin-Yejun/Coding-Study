import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = input().strip()
    k = int(input())

    d = defaultdict(list)
    left, right = 0, 0
    for i in range(len(s)):
        d[s[i]].append(i)

    d = {key: val for key, val in d.items() if len(val) >= k}
    result = []
    for val in d.values():
        for i in range(len(val) - (k-1)):
            result.append(val[i+k-1] - val[i])
    if result:
        print(min(result)+1, max(result)+1)
    else:
        print(-1)