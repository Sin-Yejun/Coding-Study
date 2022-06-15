D = int(input())
N, M, K = map(int,input().split())

total_mandoo = []
mixed_rice = []

A = D - N%D
B = D - M%D
total_mandoo.append(N//D + M//D + K//D)
mixed_rice.append(K)

total_mandoo.append((N+A)//D + M//D + (K-A)//D)
mixed_rice.append(K-A)

total_mandoo.append(N//D + (M+B)//D + (K-B)//D)
mixed_rice.append(K-B)

total_mandoo.append((N+A)//D + (M+B)//D + (K-A-B)//D)
mixed_rice.append(K-A-B)

ZIP = list(zip(total_mandoo, mixed_rice))
ZIP.sort(key = lambda x:(-x[0],-x[1]))
print(ZIP[0][1])
