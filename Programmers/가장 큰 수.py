# https://jokerldg.github.io/algorithm/2021/05/06/most-big-number.html
def solution(numbers):
    arr = list(map(str,numbers))
    arr.sort(key= lambda x:x*3 ,reverse = True)
    return str(int(''.join(arr)))
