def is_triangle(a,b,c):
    arr = [a,b,c]
    arr.sort()
    if arr[0]+arr[1] > arr[2]:
        return True
    else:
        return False

while True:
    a, b, c = map(int,input().split())
    if a==b==c==0:
        break
    if not is_triangle(a,b,c):
        print('Invalid')
    else:
        if a==b==c:
            print('Equilateral')
        elif a==b or b==c or a==c:
            print('Isosceles')
        else:
            print('Scalene')
