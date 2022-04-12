s = input()

pv = ''
Max = len(s)*10

for i in s:
    if pv == i:
        Max -= 5
    pv = i

print(Max)
