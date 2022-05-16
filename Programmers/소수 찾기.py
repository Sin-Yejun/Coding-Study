from itertools import permutations
import math
def check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    l = len(numbers)
    arr = list(numbers)
    all_arr = []
    result = set()
    for i in range(1, l+1):
        temp = list(permutations(arr,i))
        for j in temp:
            num = int(''.join(j))
            if check(num):
                result.add(num)
    
    return len(result)
