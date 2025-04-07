import sys, bisect
from collections import defaultdict
input = sys.stdin.readline

def add_func(num, deg):
    d[num] = deg
    if deg not in degrees:
        bisect.insort(arr, deg)
    degrees[deg].add(num)

def solved_func(num):
    deg = d.pop(num)
    degrees[deg].remove(num)
    if not degrees[deg]:
        del degrees[deg]

def recommend_func(num):
    if num == 1:
        for i in range(len(arr)-1, -1, -1):
            deg = arr[i]
            if deg in degrees:
                print(max(degrees[deg]))
                return
    else:
        for i in range(len(arr)):
            deg = arr[i]
            if deg in degrees:
                print(min(degrees[deg]))
                return


n = int(input())
d = {}
degrees = defaultdict(set)
arr = []
for i in range(n):
    number, degree = map(int, input().split())
    add_func(number, degree)

m = int(input())
for i in range(m):
    line = list(input().split())
    if line[0] == 'add':
        add_func(int(line[1]), int(line[2]))
    elif line[0] == 'recommend':
        recommend_func(int(line[1]))
    else:
        solved_func(int(line[1]))
