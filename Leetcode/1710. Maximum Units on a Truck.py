class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x:x[1], reverse = True)
        cnt = 0
        total = 0
        for i in range(len(boxTypes)):
            if cnt+boxTypes[i][0] > truckSize:
                total += (truckSize-cnt) * boxTypes[i][1]
                break
            else:
                total += boxTypes[i][0]*boxTypes[i][1]
                cnt += boxTypes[i][0]
            
        return total
