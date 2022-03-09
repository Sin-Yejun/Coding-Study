money = 1000 - int(input())
left = [500, 100, 50, 10, 5, 1]
idx = 0
cnt = 0
while money != 0:
    if money >= left[idx]:
        money -= left[idx]
        cnt += 1
    else:
        idx += 1
print(cnt)
    
