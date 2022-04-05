# https://leetcode.com/problems/reverse-bits/discuss/54740/Python-AC-with-63ms-3lines
class Solution:
    def reverseBits(self, n: int) -> int:
        oribin='{0:032b}'.format(n)
        print(oribin)
        oribin = oribin[::-1]
        return int(oribin,2)
