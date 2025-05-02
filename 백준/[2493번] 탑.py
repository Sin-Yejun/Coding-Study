n = int(input())
arr = list(map(int, input().split()))
stack = []
answer = []
for idx, val in enumerate(arr, 1):
    if not stack:
        stack.append((idx, val))
        answer.append(0)
        continue
    while stack:
        if val < stack[-1][1]:
            break
        i, v = stack.pop()
    if stack:
        answer.append(stack[-1][0])
    else:
        answer.append(0)
    stack.append((idx, val))
print(*answer)

    