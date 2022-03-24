# https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-11725%EB%B2%88-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EB%B6%80%EB%AA%A8-%EC%B0%BE%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

Tree = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int,input().split())
    Tree[a].append(b)
    Tree[b].append(a)

def DFS(start):
    for i in Tree[start]:
        if parents[i] == 0:
            parents[i] = start
            DFS(i)
    
DFS(1)
for i in range(2, len(parents)):
    print(parents[i])

