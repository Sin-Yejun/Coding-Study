class Solution:
    def capitalizeTitle(self, title: str) -> str:
        arr = list(title.split(' '))
        new_arr = []
        for i in arr:
            s = i.lower()
            if len(i) <= 2:
                new_arr.append(s)
            else:
                c = chr(ord(s[0])-32)
                s = c + s[1:]
                new_arr.append(s)
        return ' '.join(new_arr)
