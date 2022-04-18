n, m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
s = []
def back_tracking():
    if len(s) == m:
        print(' '.join(map(str,s)))
    else:
        for i in arr:
            if s and s[-1] > i:
                continue
            s.append(i)
            back_tracking()
            s.pop()

back_tracking()
            
