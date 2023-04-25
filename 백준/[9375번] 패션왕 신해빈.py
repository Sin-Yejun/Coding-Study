from collections import defaultdict

T = int(input())

for _ in range(T):
    n = int(input())
    d = defaultdict(list)
    for __ in range(n):
        name, cat = input().split()
        d[cat].append(name)
    ans = 1
    for key, val in d.items():
        ans *= len(val)+1
    print(ans-1)
    
   
    
        
