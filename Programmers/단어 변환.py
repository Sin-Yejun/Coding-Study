from collections import defaultdict

def check(word1, word2):        # 1개의 알파벳만 다른 문자 확인
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    graph = defaultdict(list)
    for i in words:
        if check(begin, i):
            graph[begin].append(i)
    for i in range(len(words)):
        temp = []
        for j in range(len(words)):
            if i != j and check(words[i], words[j]):
                temp.append(words[j])
        graph[words[i]] = temp
        
    stack = [begin]
    cnt = 0
    while stack:
        if stack[-1] in graph:
            if target in graph[stack[-1]]:
                return cnt+1
            stack.append(graph[stack.pop()].pop())
            cnt += 1
    
    
