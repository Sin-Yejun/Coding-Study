# https://seongonion.tistory.com/53
import sys
input = sys.stdin.readline
st1 = list(input().rstrip())
st2 = []

for _ in range(int(input())):
    cmd = list(input().rstrip().split())
    if cmd[0] == 'L':
        if st1:
            st2.append(st1.pop())
        
    elif cmd[0] == 'D':
        if st2:
            st1.append(st2.pop())

    elif cmd[0] == 'B':
        if st1:
            st1.pop()
        
    else:
        st1.append(cmd[1])
        
st1.extend(reversed(st2))
print(''.join(st1))
