import sys
city = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))

sum_price = 0
m = price[0]
for i in range(city-1):
    if price[i] < m:
        m = price[i]
    sum_price += m*distance[i]
print(sum_price)