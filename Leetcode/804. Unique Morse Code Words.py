class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = set()
        for i in words:
            temp = ""
            for j in i:
                temp += morse[ord(j)-97]
            ans.add(temp)
        
        return len(ans)
            
                
