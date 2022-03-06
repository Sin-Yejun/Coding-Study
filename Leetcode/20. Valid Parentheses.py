class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')':
                if '(' not in stack:
                    return False
                if stack[-1] != '(':
                    return False
                del stack[-1]
            elif i == '}':
                if '{' not in stack:
                    return False
                if stack[-1] != '{':
                    return False
                del stack[-1]
            elif i == ']':
                if '[' not in stack:
                    return False
                if stack[-1] != '[':
                    return False
                del stack[-1]
            
        if len(stack) == 0:
            return True
        else:
            return False
