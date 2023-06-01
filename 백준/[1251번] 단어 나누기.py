word = list(input())
res = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        first = word[:i] # 첫 번째 단어
        second = word[i:j] # 두 번째 단어
        third = word[j:] # 세 번째 단어
      
        first.reverse()
        second.reverse()
        third.reverse()

        res.append("".join(first + second + third))

print(min(res))
