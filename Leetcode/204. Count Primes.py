class Solution:
    def countPrimes(self, n: int) -> int:
       
        che = [True]*n

        m = int(n**0.5)

        for i in range(2,m+1):
            if che[i]:
                for j in range(i+i,n,i):
                    che[j] = False
        cnt = 0
        for i in range(2,len(che)):
            if che[i] == True:
                cnt += 1
        return cnt
