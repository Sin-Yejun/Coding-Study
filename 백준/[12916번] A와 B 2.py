from collections import deque
s = input().strip()
t = input().strip()


def dfs(x):
    if x == s:
        return True
    if len(x) < len(s):
        return False
    
    res = False
    if x[-1] == 'A':    #뒤에 A가 붙은 경우
        res |= dfs(x[:-1])
    if x[0] == 'B':
        res |= dfs(x[1:][::-1])
    return res

if dfs(t):
    print(1)
else:
    print(0)