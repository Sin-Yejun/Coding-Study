def getMyDivisor(n):
    divisorsList = []
    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)
    divisorsList.sort() 
    return divisorsList

n, k = map(int, input().split())
arr = getMyDivisor(n)
if len(arr) < k:
    print(0)
else:
    print(arr[k-1])
