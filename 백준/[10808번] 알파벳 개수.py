n = input()
arr = [0 for i in range(26)]
for i in n:
    arr[ord(i)-97] += 1
print(' '.join(map(str,arr)))
