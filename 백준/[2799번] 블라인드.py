m, n = map(int,input().split())
b1 = '................'
b2 = '****............'
b3 = '********........'
b4 = '************....'
b5 = '****************'
b_index1 = 0
b_index2 = 0
b_index3 = 0
b_index4 = 0
b_index5 = 0
arr = [['' for col in range(n)] for row in range(m)]
line = 0
count = 0
index = 0
for _ in range(5*m+1):
    line = input().split('#')
    try:
        while True:
            line.remove('')
    except ValueError:
        pass

    if len(line) != 0:
        count += 1
        for i in range(n):
            arr[index][i] += line[i]
        if count %4 == 0:
            index += 1

for i in range(m):
    for j in range(n):
        if arr[i][j] == b1:
            b_index1 += 1
        elif arr[i][j] == b2:
            b_index2 += 1
        elif arr[i][j] == b3:
            b_index3 += 1
        elif arr[i][j] == b4:
            b_index4 += 1
        elif arr[i][j] == b5:
            b_index5 += 1
print(b_index1, b_index2, b_index3, b_index4, b_index5) 
            

            
