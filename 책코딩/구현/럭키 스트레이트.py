n = input()
lucky = False
for i in range(1, len(n)):
    x = list(map(int, n[:i]))
    y = list(map(int, n[i:]))
    if sum(x) == sum(y):
        lucky = True
if lucky:
    print('LUCKY')
else:
    print('READY')
    
    