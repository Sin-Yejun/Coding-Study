class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [True] + [False] * (len(rooms)-1)
        arr = rooms[0]
        while arr:
            x = arr.pop()
            if visited[x]:
                continue
            else:
               visited[x] = True
               arr.extend(rooms[x])
            
        if False in visited:
            return False
        else:
            return True
