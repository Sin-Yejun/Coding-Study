# https://chancoding.tistory.com/49
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    inp = sys.stdin.readline().strip()
    left = []
    right = []
    for i in inp:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    left.extend(reversed(right))
    print(''.join(left))
            
    
