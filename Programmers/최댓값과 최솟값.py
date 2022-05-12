def solution(s):
    arr = list(map(int,s.split()))
    arr.sort()
    ans = str(arr[0])+' '+str(arr[-1])
    return ans
