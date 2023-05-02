## 조합 사용방법

from itertools import permutations
import sys

input = sys.stdin.readline
'''
n, m = map(int, input().split())
numbers = list(map(int, input().split()))

# 주어진 수열을 사전순으로 정렬합니다.
numbers.sort()

# permutations 함수를 이용하여 길이가 M인 순열을 구합니다.
# set을 이용하여 중복되는 수열을 제거합니다.
result = set(permutations(numbers, m))

# 결과를 사전순으로 정렬하고 출력합니다.
for seq in sorted(result):
    print(*seq)

'''
## 백트래킹 사용방법

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
visited = [False] * n  # 각 수가 사용되었는지 확인하는 리스트
sequence = []  # 만들어진 수열을 저장하는 리스트

# 주어진 수열을 사전순으로 정렬합니다.
numbers.sort()

def dfs(depth, start):
    if depth == m:
        # 수열이 완성되면 출력합니다.
        print(*sequence)
        return

    used = set()  # 이미 사용한 수를 저장하는 집합

    for i in range(start, n):
        if not visited[i] and numbers[i] not in used:
            # i번째 수가 사용되지 않았고, 이전에 사용한 적이 없는 수라면 수열에 추가합니다.
            visited[i] = True
            sequence.append(numbers[i])
            used.add(numbers[i])

            # 다음 자리 수를 탐색합니다.
            dfs(depth + 1, i + 1)

            # 탐색이 종료되면 수열에서 제거하고 사용 여부를 변경합니다.
            sequence.pop()
            visited[i] = False

dfs(0, 0)
