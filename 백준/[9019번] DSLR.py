import sys
from collections import deque
input = sys.stdin.readline

def D(n):
    return (2*n)%10000
def S(n):
    if n == 0:
        return 9999
    return n-1
def L(n):
    
    return (10*n+(n//1000))%10000

def R(n):
    
    return (n//10+(n%10)*1000)%10000

n = int(input())
for _ in range(n):
    visited = [False]*10001
    a, b = map(int, input().split())
    q = deque([(a, '')])
    while q:
        x, c = q.popleft()
        visited[x] = True
        if x == b:
            print(c)
            break
        output = D(x)
        if not visited[output]:   
            q.append((output, c+'D'))
            visited[output] = 1
        output = S(x)
        if not visited[output]:   
            q.append((output, c+'S'))
            visited[output] = 1
        output = L(x)
        if not visited[output]:   
            q.append((output, c+'L'))
            visited[output] = 1
        output = R(x)
        if not visited[output]:   
            q.append((output, c+'R'))
            visited[output] = 1
