class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a','e','i','o','u','A','E','I','O','U']
        vowels = []
        ans = ''
        for i in s:
            if i in vowel:
                vowels.append(i)
        for i in s:
            if i in vowel:
                ans += vowels.pop()
            else:
                ans += i
        return ans
