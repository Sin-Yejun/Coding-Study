n = int(input())
word = []
for i in range(n):
    word.append(input())
for i in range(n):
    print('String #%d'%(i+1))
    for j in word[i]:
        if ord(j)==90:
            print('A',end='')
        else:
            print(chr(ord(j)+1),end='')
    print()
    if i!=n-1:
        print()
