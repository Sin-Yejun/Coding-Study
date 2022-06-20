# https://inspirit941.tistory.com/101
def solution(n, s):
    if n > s:
        return [-1]
    
    val = s // n
    arr = []
    for i in range(n):
        arr.append(val)
    idx = len(arr)-1
    for i in range(s%n):
        arr[idx] += 1
        idx -= 1
    return arr
