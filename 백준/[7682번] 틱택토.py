import sys
input = sys.stdin.readline

def complete(s):
    x_win = False
    o_win = False
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # 가로
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # 세로
        (0, 4, 8), (2, 4, 6)              # 대각선
    ]
    for a, b, c in lines:
        if s[a] == s[b] == s[c]:
            if s[a] == 'X':
                x_win = True
            elif s[a] == 'O':
                o_win = True
    return x_win, o_win

while True:
    s = input().strip()
    if s == 'end':
        break
    x = s.count('X')
    o = s.count('O')
    dots = s.count('.')

    if o > x or x > o + 1:
        print('invalid')
        continue

    x_win, o_win = complete(s)

    if x_win and o_win:
        print('invalid')
    elif x_win:
        if x == o + 1:
            print('valid')
        else:
            print('invalid')
    elif o_win:
        if x == o:
            print('valid')
        else:
            print('invalid')
    else:
        if dots == 0 and x == 5 and o == 4:
            print('valid')
        else:
            print('invalid')
