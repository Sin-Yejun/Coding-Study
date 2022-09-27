# https://leetcode.com/problems/push-dominoes/discuss/132330/funny-idea-but-passed-within-time-limit-(Python)
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
            while(True):
                new = dominoes.replace('R.L', 'S')
                new = new.replace('.L','LL').replace('R.','RR')
                if new == dominoes:
                    break
                else:
                    dominoes = new
            return dominoes.replace('S', 'R.L')
