class Solution:
    def makeGood(self, s: str) -> str:
        arr = list(s)
        i = 0
        while True:
            first = len(arr)
            for i in range(len(arr)-1):
                if abs(ord(arr[i]) - ord(arr[i+1])) == 32:
                    arr = arr[:i]+arr[i+2:]
                    break
            last = len(arr)
            if first == last:
                break

        return ''.join(arr)
            