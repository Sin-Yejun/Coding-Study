#https://somjang.tistory.com/entry/leetCode-686-Repeated-String-Match-Python
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        len_a = len(a)
        len_b = len(b)
        answer = len_b // len_a +2
        temp = a*answer
        if b not in temp:
            return -1
        while True:
            if b in a * (answer-1):
                answer -= 1
            else:
                break
        return answer
