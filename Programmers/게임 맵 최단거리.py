from collections import deque

def solution(maps):
    def BFS(x,y,cnt):
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        
        queue.append([x,y,cnt])
        while queue:
            tmp = queue.popleft()
            if tmp[0] == len(visited)-1 and tmp[1] == len(visited[0])-1:
                queue.clear()
                return tmp[2]
            for i in range(4):
                rx = tmp[0] + dx[i]
                ry = tmp[1] + dy[i]
                if 0<= rx < len(visited) and 0<= ry < len(visited[0]):
                    if visited[rx][ry]:
                        visited[rx][ry] = False
                        queue.append([rx,ry,tmp[2]+1])
        return -1
    queue = deque()
    visited = []
    for i in maps:
        temp = []
        for j in i:
            if j:
                temp.append(True)
            else:
                temp.append(False)
        visited.append(temp)
    return BFS(0,0,1)
