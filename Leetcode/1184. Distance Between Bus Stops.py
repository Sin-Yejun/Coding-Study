class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start == destination:
            return 0
        tot = 0
        counter_tot = 0
        
        if start < destination:
            for i in range(start, destination):
                tot += distance[i]
            counter_tot = sum(distance) - tot
        else:
            for i in range(destination, start):
                tot += distance[i]
            counter_tot = sum(distance) - tot
        
        return min(tot, counter_tot)
        
            
        
