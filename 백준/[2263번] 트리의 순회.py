import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
in_order = [-1]+list(map(int,input().split()))
post_order = [-1]+list(map(int,input().split()))
# 인오더를 분할하기 위해 매번 n번 탐색하면 
# 시간 초과가 발생할 것이므로 미리 위치를 저장해준다.
pos = [-1]*(n+1) 
for i in range(n+1):
    pos[in_order[i]] = i
ans = []

def daq(in_start,in_end,post_start,post_end):
    if (in_start > in_end) or (post_start > post_end):
        return
    root = post_order[post_end]
    size = pos[root] - in_start
    ans.append(root)
    
    daq(in_start, pos[root]-1, post_start, post_start + size - 1)
    daq(pos[root]+1, in_end, post_start + size, post_end - 1)

daq(1,n,1,n)
print(*ans)
