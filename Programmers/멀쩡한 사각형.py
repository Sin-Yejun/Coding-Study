def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
        
def solution(w,h):

    return w*h - (w+h-gcd(w,h))
