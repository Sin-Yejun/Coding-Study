# 각 숫자의 차의 최대공약수를 구함.(나머지를 없애주기 위해)
# 마지막으로 나온 최대공약수의 약수를 구하면 답
# https://pacific-ocean.tistory.com/224
import sys
def GCD(a,b):
    while b!=0:
        a, b = b, a%b
    return a
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
g = 0
for i in range(len(arr)):
    if i == 1:
        g = abs(arr[1]-arr[0])
    g = GCD(abs(arr[i]-arr[i-1]),g)
divisor_arr = []
for i in range(1, int(g**(1/2))+1): # 약수 구할때 시간복잡도 O(N의 제곱근) 알고리즘
    if g%i == 0:
        divisor_arr.append(i)
        if i**2 != g:
            divisor_arr.append(g//i)

divisor_arr.sort()
divisor_arr.remove(1)
print(' '.join(map(str,divisor_arr)))
        
    

