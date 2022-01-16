# https://chancoding.tistory.com/44 (이분탐색 이용)
import sys
n = int(sys.stdin.readline())
n_list = sorted(list(map(int,sys.stdin.readline().split())))
m = int(sys.stdin.readline())
m_list = list(map(int,sys.stdin.readline().split()))

def binary(l, n_list, start, end):
    if start > end:
        return 0
    m = (start+end) // 2
    if l == n_list[m]:
        return 1
    elif l < n_list[m]:
        return binary(l, n_list, start, m-1)
    else:
        return binary(l, n_list, m+1, end)

for l in m_list:
    start = 0
    end = len(n_list)-1
    print(binary(l,n_list,start,end))
