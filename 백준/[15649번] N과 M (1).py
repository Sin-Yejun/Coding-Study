# https://jamesu.dev/posts/2020/04/13/baekjoon-problem-solving-15649/
n, m = map(int, input().split())

s = []
def dfs():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1):
    if i in s:
      continue
    s.append(i)
    dfs()
    s.pop()

dfs()
