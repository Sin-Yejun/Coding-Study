n = int(input())
cnt = 0
num = 665
while True:
    num += 1
    if '666' in str(num):
        cnt += 1
    if cnt == n:
        print(num)
        break
