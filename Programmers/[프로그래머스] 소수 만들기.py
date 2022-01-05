import math
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
def solution(nums):
    answer = 0
    for i in range(nums-2):
        for j in range(i+1, nums-1):
            for k in range(j+1, nums):
                if is_prime_number(nums[i]+nums[j]+nums[k]) == True:
                    answer += 1

    return answer

solution([1,2,3,4])
