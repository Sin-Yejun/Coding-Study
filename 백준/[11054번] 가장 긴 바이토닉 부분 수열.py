# https://seohyun0120.tistory.com/entry/%EB%B0%B1%EC%A4%80-11054-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EB%B0%94%EC%9D%B4%ED%86%A0%EB%8B%89-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%92%80%EC%9D%B4
x = int(input())
arr = list(map(int, input().split()))
reverse_arr = arr[::-1]

increase = [1 for _ in range(x)]
decrease = [1 for _ in range(x)]

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reverse_arr[i] > reverse_arr[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)
result = [0 for _ in range (x)]
for i in range(x):
    result[i] = increase[i] + decrease[x-i-1] - 1

print(max(result))
