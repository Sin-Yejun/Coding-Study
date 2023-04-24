from math import sqrt

n = int(input())

# 제곱수 1개

if int(sqrt(n)) == sqrt(n):
    print(1)
    exit()
# 제곱수 2개

for i in range(1, int(sqrt(n))+1):
    if int(sqrt(n - i**2)) == sqrt(n - i**2):
        print(2)
        exit()
        
# 제곱수 3개
for i in range(1, int(sqrt(n))+1):
    for j in range(1, int(sqrt(n-i**2))+1):
        if int(sqrt(n - i**2 - j**2)) == sqrt(n-i**2-j**2):
            print(3)
            exit()

# 제곱수 4개

print(4)
