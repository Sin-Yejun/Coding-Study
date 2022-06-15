from collections import deque

n = input()
arr = deque(n)
answer = 0
for i in range(len(n)):
    arr.rotate(1)
    temp = int(''.join(arr))
    answer += temp

print(answer)
