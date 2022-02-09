# https://leetcode.com/problems/simplify-path/discuss/1051132/Simplify-Path-or-Easy-Python-Solution
class Solution:
    def simplifyPath(self, path: str) -> str:

            stack = []
            path = path.split('/')
            for p in path:
                if not p or p=='.':
                    continue
                elif p=='..':
                    if stack:
                        stack.pop()
                else:
                    stack.append(p)


            root = "/"

            return root + "/".join(stack)
        
