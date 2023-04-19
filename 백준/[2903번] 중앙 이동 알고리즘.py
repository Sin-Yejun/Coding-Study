import math
n = int(input())
arr = [4]
for i in range(1, 16):
    temp = arr[i-1]+ (math.pow(2,i)+1)*math.pow(2,i) - math.pow(4,i-1)
    arr.append(int(temp))
print(arr[n])
