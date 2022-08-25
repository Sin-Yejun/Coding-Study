class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        answer = 0
        for i in range(n):
            answer += mat[i][i]
            answer += mat[i][n-i-1]
        if n % 2 == 1:
            answer -= mat[n//2][n//2]
        return answer
