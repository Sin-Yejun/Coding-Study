def solution(s):
    ans = ''
    idx = 0
    for i in range(len(s)):
        if s[i] == ' ':
            idx = 0
            ans += ' '
        else:
            if idx %2 == 0:
                ans += s[i].upper()
            else:
                ans += s[i].lower()
            idx += 1
    return ans
