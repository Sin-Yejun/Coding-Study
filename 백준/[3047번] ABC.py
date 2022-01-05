dic = {}
arr = list(map(int,input().split()))
arr.sort()
dic['A'] = arr[0]
dic['B'] = arr[1]
dic['C'] = arr[2]

arr2 = list(map(str,input()))
for i in arr2:
    print(dic[i], end=' ')
