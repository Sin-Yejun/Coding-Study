n = int(input())
m = int(input())
s = input()

p = 'I' + 'OI'*n
table = [0]+[x for x in range(m+1)]
count = 0
i = 0
for j in range(len(s)):
    while i > 0 and p[i] != s[j]:
        i = table[i-1]
    if p[i] == s[j]:
        i += 1
        if i == len(p):
            i = table[i-1]
            count += 1
print(count)

