class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            if t == '+':
                x = nums.pop()
                y = nums.pop()
                nums.append(x+y)
            elif t == '-':
                x = nums.pop()
                y = nums.pop()
                nums.append(y-x)
            elif t == '*':
                x = nums.pop()
                y = nums.pop()
                nums.append(x*y)
            elif t == '/':
                x = nums.pop()
                y = nums.pop()
                nums.append(int(y/x))
            else:
                nums.append(int(t))
        return nums[0]
