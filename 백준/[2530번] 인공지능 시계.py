a, b, c = map(int,input().split())
sec = int(input())

c += sec % 60
b += c // 60 + sec//60%60
a += b // 60 + sec//60//60

print(a%24, b % 60, c % 60)
