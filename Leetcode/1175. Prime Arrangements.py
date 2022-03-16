# https://leetcode.com/problems/prime-arrangements/discuss/371862/JavaPython-3-two-codes-each-count-only-primes-then-compute-factorials-for-both-w-analysis.
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        cnt = 1                                                     # number of primes, first prime is 2.
        for i in range(3, n + 1, 2):                                # only odd number could be a prime, if i > 2.
            factor = 3
            while factor * factor <= i:
                if i % factor == 0:
                    break 
                factor += 2    
            else:
                cnt += 1
        return math.factorial(cnt) * math.factorial(n - cnt) % (10**9 + 7)
