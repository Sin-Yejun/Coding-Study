n = int(input())
Max = 0
for _ in range(n):
    s = input()
    Max = max(Max, s.count('for') + s.count('while'))
print(Max)
