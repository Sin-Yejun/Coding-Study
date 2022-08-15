class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1]]
        for i in range(numRows-1):
            temp = [1]
            for j in range(1, len(arr[i])):
                temp.append(arr[i][j-1]+arr[i][j])
            temp.append(1)
            arr.append(temp)
        return arr
