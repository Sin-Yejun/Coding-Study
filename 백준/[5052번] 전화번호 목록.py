import sys
input = sys.stdin.readline

def is_consistent(phone_numbers):
    trie = {}

    for number in phone_numbers:
        node = trie
        for ch in number:
            if '#' in node:  # 다른 번호가 이 번호의 접두사
                return False
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        if node:  # 이 번호가 다른 번호의 접두사
            return False
        node['#'] = True  # 이 번호 끝 표시
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    phone_numbers = [input().strip() for _ in range(n)]
    result = is_consistent(phone_numbers)
    print("YES" if result else "NO")
