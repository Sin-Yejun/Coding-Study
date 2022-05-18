# https://eunhee-programming.tistory.com/145
def solution(n,a,b): 
    cnt=0 
    while True: 
        a= (a//2)+(a%2) 
        b= (b//2)+(b%2) 
        cnt+=1 
        if a==b: 
            break 
    return cnt
