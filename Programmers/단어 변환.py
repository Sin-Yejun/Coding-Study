from collections import defaultdict
from collections import deque
begin, target, words = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
words = [begin] + words
d = defaultdict(list)
start = begin
for i in range(len(words)):
    temp = []
    for j in range(len(words)):
        cnt = 0
        if i != j:
            for k in range(len(begin)):
                if words[i][k]  == words[j][k]:
                    cnt += 1
        else:
            cnt
        temp.append(len(begin)-cnt)
    d[words[i]] = temp

q = deque([(begin, d[begin], 0)])

while q:
    w, path, cnt = q.popleft()
    print(w, path, cnt)
    if w == target:
        print(cnt)
        break
    for i in range(len(path)):
        if path[i] == 1:
            path[i] -= 1
            q.append((words[i], d[words[i]], cnt + 1))
