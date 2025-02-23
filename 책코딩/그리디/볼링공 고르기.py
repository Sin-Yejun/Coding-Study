import time

n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

st1 =  time.perf_counter()
answer = 0
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] != arr[j]:
            answer+=1
ed1 = time.perf_counter()
print(answer)

'''
책풀이
'''

st2 = time.perf_counter()
array = [0]*11
for x in arr:
    array[x] += 1

result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i]*n
ed2 = time.perf_counter()
print(result)

print(ed1-st1)
print(ed2-st2)