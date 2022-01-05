while True:
    s = input()
    if s=='0':
        break
    elif s==s[::-1]:
        print('yes')
    else:
        print('no')
