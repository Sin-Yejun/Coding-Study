n, m = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = max(arr)
while start <= end:
    total = 0
    mid = (start+end)//2
    for x in arr:
        if x > mid:
            total += x - mid
    
    # 떡의 양이 부족한 경우 더 많이 자르기
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기
    else:
        result = mid
        start = mid + 1
print(result)
    