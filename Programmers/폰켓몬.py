def solution(nums):
    choose = len(nums)//2
    nums = set(nums)
    if len(nums) < choose:
        return len(nums)
    else:
        return choose
