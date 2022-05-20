from itertools import product
def solution(word):
    vowel = ['A', 'E', 'I', 'O', 'U']
    arr = []
    cnt = 0
    for i in range(1, 6):
        for per in product(vowel, repeat = i):
            cnt += 1
            tmp = ''.join(per)
            arr.append(tmp)
    arr.sort()
    for i in range(len(arr)):
        if word == arr[i]:
            return i+1
