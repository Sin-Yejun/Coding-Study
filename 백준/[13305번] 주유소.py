import sys
city = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))
if sum(distance) > 10000:
    exit(0)
if max(price) > 10000:
    exit(0)
sum_price = 0
m = price[0]
for i in range(city-1):
    if price[i] < m:
        m = price[i]
    sum_price += m*distance[i]
print(sum_price)
