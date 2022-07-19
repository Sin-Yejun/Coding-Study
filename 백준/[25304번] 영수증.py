total = int(input())
n = int(input())
val = 0
for _ in range(n):
    price, item = map(int, input().split())
    val += price*item
if total == val:
    print('Yes')
else:
    print('No')
