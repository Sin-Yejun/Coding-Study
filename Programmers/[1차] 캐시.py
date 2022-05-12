from collections import deque
def solution(cacheSize, cities):
    cities = list(map(lambda x:x.lower(), cities))
    if cacheSize == 0:
        return 5*len(cities)
    queue = deque()
    time = 0
    for city in cities:
        if city in queue:       # Hit
            queue.remove(city)
            queue.append(city)
            time += 1
        else:                   # Miss
            if len(queue) == cacheSize:
                queue.popleft()
            queue.append(city)
            time += 5
    return time
                
    
