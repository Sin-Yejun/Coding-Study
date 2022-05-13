def gcd(a,b):
    while b > 0:
        a, b = b, a%b
    return a
def lcm(a,b):
    return a * b // gcd(a,b)
def solution(arr):
    if len(arr) == 1:
        return arr[0]
    while len(arr) != 1:
        x = arr.pop()
        y = arr.pop()
        arr.append(lcm(x,y))
    return arr[0]
