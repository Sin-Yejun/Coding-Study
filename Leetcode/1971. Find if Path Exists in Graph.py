class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1:
            return True
        line = [[] for _ in range(n)]
        for x, y in edges:
            line[x].append(y)
            line[y].append(x)
    
        arr = line[source]
        visited = [False] * (n)
        while arr:
            x = arr.pop()
            if visited[x] == False:
                visited[x] = True
                arr.extend(line[x])
        return visited[destination]
            
