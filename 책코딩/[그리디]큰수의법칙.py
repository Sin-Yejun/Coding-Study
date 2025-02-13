N, M, K = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort(reverse=True)
a = n_list[0]
b = n_list[1]
# cnt = 0
# ans = 0
# for i in range(1, M+1):
#     if i % K == 0:
#         ans += b
#     else:
#         ans += a
# print(ans)
count = int(M/(K+1))*K
count += M % (K+1)
ans = 0
ans += count*a
ans += (M-count)*b
print(ans)