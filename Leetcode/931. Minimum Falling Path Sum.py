class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        N = len(matrix)
        for i in range(1, N):
            for j in range(N):
                if j == 0:
                    matrix[i][j] += min(matrix[i-1][j], matrix[i-1][j+1])
                elif j == N-1:
                    matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j])
                else:
                    matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j], matrix[i-1][j+1])
        return min(matrix[N-1])