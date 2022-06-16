import sys
input = sys.stdin.readline
n = int(input())
person = [1, 1]
for i in range(n):
    op1, op2 = input().split()
    if person[0] > 0:
        c = max(int(eval(str(person[0])+op1)), int(eval(str(person[0])+op2)))
    d = max(int(eval(str(person[1])+op1)), int(eval(str(person[1])+op2)))

    person[1] = max(person[0],d)
    person[0] = c
    if max(person) <= 0:
        print('ddong game')
        break
else:
    print(max(person))
