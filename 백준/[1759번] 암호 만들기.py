from itertools import combinations

n, m = map(int,input().split())
arr = list(input().split())
arr.sort()
comb = list(combinations(arr,n))

vowel = ['a','e','i','o','u']
word = []
for i in comb:
    v = 0
    c = 0
    for j in i:
        if j in vowel:
            v += 1
        else:
            c += 1
    if v > 0 and c > 1:
        word.append(i)

for i in word:
    print(''.join(i))
