class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        T_matrix = []
        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            T_matrix.append(temp)
        return T_matrix
