n = 6
cores = [1,2, 3]

left, right = 0, max(cores)*n
while left <= right:
    mid = (left+right)//2
    total = sum([mid // core + 1 for core in cores])
    if total >= n:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1
    
    total = sum([(answer-1)// core + 1 for core in cores])
    remain = n - total

    for i, core in enumerate(cores):
        if answer % core == 0:
            remain -= 1
            if remain == 0:
                print(i+1)
                break
    