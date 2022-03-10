class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char = ['b','a','l','o','n']
        temp = [0,0,0,0,0]
        for i in range(len(text)):
            if text[i] in char:
                temp[char.index(text[i])] += 1
        output = 0
        while temp[0]>0 and temp[1] > 0 and temp[2] > 1 and temp[3] > 1 and temp[4] > 0:
            temp[0] -= 1; temp[1] -= 1; temp[2] -= 2; temp[3] -= 2; temp[4] -= 1;
            output += 1
        
        return output
