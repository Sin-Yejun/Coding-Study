class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0 = coordinates[0][0]
        y0 = coordinates[0][1]
        x1 = coordinates[1][0]
        y1 = coordinates[1][1]
        
        for x, y in coordinates:
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                    return False
        return True
