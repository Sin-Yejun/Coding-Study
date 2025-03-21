sticker = [14, 16, 1]
dp1 = sticker[:-1]
dp2 = sticker[1:]
n = len(sticker) - 1
for i in range(2, n):
    if i == 2:
        dp1[i] += dp1[i-2]
        dp2[i] += dp2[i-2]
    else:
        dp1[i] += max(dp1[i-2], dp1[i-3])
        dp2[i] += max(dp2[i-2], dp2[i-3])

print(max(max(dp1), max(dp2)))