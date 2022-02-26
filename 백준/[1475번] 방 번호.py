# https://bgspro.tistory.com/62
n = int(input())
arr = list(map(int,str(n)))

temp = [0]*10

for i in range(len(arr)):
    if arr[i] == 6 or arr[i] == 9:
        if temp[6] <= temp[9]:
            temp[6] += 1
        else:
            temp[9] += 1
    else:
        temp[arr[i]] += 1
print(max(temp))
