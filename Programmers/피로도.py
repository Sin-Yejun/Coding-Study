
def solution(k, dungeons):
    def dfs(k, cnt):
        if cnt > answer[0]:
            answer[0] = cnt
        for j in range(N):
            if k >= dungeons[j][0] and not visited[j]:
                visited[j] = 1
                dfs(k - dungeons[j][1], cnt + 1)
                visited[j] = 0
    answer = [0]
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0)
    return answer[0]
