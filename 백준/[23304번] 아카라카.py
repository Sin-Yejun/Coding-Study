def aka(string):
    half = len(string)//2
    if string == string[::-1]:
        pre = string[:half]
        pro = string[half+1:]
        if pre == pre[::-1] and pro == pro[::-1]:
            
string = input()
half = len(string)//2
if string == string[::-1]:
    pre = string[:half]
    pro = string[half+1:]
    if pre == pre[::-1] and pro == pro[::-1]:
        print('AKARAKA')
    else:
        print('IPSELENTI')
else:
    print('IPSELENTI')
