import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
d = defaultdict(list)
for _ in range(n):
    a, b, c = input().strip().split()
    d[a] = [b,c]
    
def preorder(node):
    if node != '.':
        print(node,end='')
        preorder(d[node][0])
        preorder(d[node][1])
    
def inorder(node):
    if node != '.':
        inorder(d[node][0])
        print(node,end='')
        inorder(d[node][1])

def postorder(node):
    if node != '.':
        postorder(d[node][0])
        postorder(d[node][1])
        print(node,end='')
preorder('A')
print()
inorder('A')
print()
postorder('A')

