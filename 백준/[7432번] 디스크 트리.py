import sys
input = sys.stdin.readline

trie = {}

def insert(path):
    node = trie
    for folder in path.split('\\'):
        if folder not in node:
            node[folder] = {}
        node = node[folder]

def print_trie(node, depth=0):
    for folder in sorted(node.keys()):
        print(' ' * depth + folder)
        print_trie(node[folder], depth + 1)
    
n = int(input())
for _ in range(n):
    insert(input().strip())

print_trie(trie)