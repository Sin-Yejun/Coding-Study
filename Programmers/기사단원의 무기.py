def solution(number, limit, power):
    def getMyDivisor(n):
        divisorsList = []
        for i in range(1, int(n**(1/2)) + 1):
            if (n % i == 0):
                divisorsList.append(i) 
                if ( (i**2) != n) : 
                    divisorsList.append(n // i)
        return len(divisorsList)
    List = []
    for i in range(1, number+1):
        n = getMyDivisor(i)
        if n > limit:
            n = power
        List.append(n)

    return sum(List)
