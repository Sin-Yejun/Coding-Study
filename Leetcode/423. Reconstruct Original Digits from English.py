# https://leetcode.com/problems/reconstruct-original-digits-from-english/discuss/1669893/Python-a-compact-solution-using-counters
class Solution:
    def originalDigits(self, s: str) -> str:
        chars = {'z': ('0', Counter('zero')), 'w': ('2', Counter('two')), 'u': ('4',Counter('four')),
                 'x': ('6', Counter('six')), 'g': ('8', Counter('eight')),'o': ('1', Counter('one')),
                 'r': ('3', Counter('three')), 'f': ('5', Counter('five')), 'v': ('7', Counter('seven')),
                 'i': ('9', Counter('nine'))}            
        result = []
        s = Counter(s)
        for char, (digit, ctr) in chars.items():
            while char in s:
                result.append(digit)
                s -= ctr
                    
        return "".join(sorted(result))
