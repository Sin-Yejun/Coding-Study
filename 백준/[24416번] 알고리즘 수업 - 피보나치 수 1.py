def recursion(n):
    
    if n == 1 or n == 2:
        return 1
    else:
        return recursion(n-1) + recursion(n-2)

def DP(n):
    cnt = 0
    arr = [1,1]
    for i in range(2, n):
        cnt += 1
        arr.append(arr[i-1] + arr[i-2])
    return cnt

n = int(input())


print(recursion(n), DP(n))
