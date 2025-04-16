import sys
input = sys.stdin.readline

# 루트 노드 정의 (딕셔너리)
trie = {}

# 트라이 삽입 함수
def insert(word):
    node = trie
    for ch in word:
        if ch not in node:
            node[ch] = {}
        node = node[ch]

# 접두사 확인 함수
def is_prefix(prefix):
    node = trie
    for ch in prefix:
        if ch not in node:
            return False
        node = node[ch]
    return True

n, m = map(int, input().split())
for _ in range(n):
    insert(input().strip())

count = 0
for _ in range(m):
    if is_prefix(input().strip()):
        count += 1
print(count)