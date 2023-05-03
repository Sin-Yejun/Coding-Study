T = input()
P = input()
i = 0
pi_arr = [0]*(len(P)+1)

for j in range(1, len(P)):
    while i > 0 and P[i] != P[j]:
        i = pi_arr[i-1]
    if P[i] == P[j]:
        i += 1
        pi_arr[j] = i

result = []
count = 0
i = 0
for j in range(len(T)):
    while i > 0 and P[i] != T[j]:
        i = pi_arr[i-1]
    if P[i] == T[j]:
        
        i += 1
        if len(P) == i:
            result.append(j-len(P)+2)
            count += 1
            i = pi_arr[i-1]

print(count)
print(' '.join(map(str,result)))
