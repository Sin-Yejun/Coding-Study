class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1], [1,1],[1,2,1]]
        if rowIndex < 3:
            return dp[rowIndex]
        for i in range(2, rowIndex):
            temp = [1]
            for j in range(len(dp[i])-1):
                temp.append(dp[i][j]+dp[i][j+1])
            temp.append(1)
            dp.append(temp)
        
        return dp[rowIndex]
