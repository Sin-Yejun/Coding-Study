class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        N = len(colors)
        flag = True
        ans = 0
        f,l = 0,0
        for i in range(0, N-1):
            if colors[i] == colors[i+1]:# 색이 연속적으로 같을 때
                if flag == True:        # 연속된 색의 시작 위치를 한번 잡아줌
                    f = i               # 연속된 색의 시작 위치
                    flag = False       
                l = i + 1               # 연속된 색의 마지막 위치 설정     
            else:
                flag = True
                if l != 0:
                    # 연속된 색깔 중 제거하는데 필요한 시간이 가장 오래걸리는 것만 남기고 제거해줌.
                    ans += sum(neededTime[f:l+1]) - max(neededTime[f:l+1])
                l = 0
                
        if l != 0:  # 마지막이 연속된 값으로 끝났을 때, ans에 더해줘야 하기 때문에
            ans += sum(neededTime[f:l+1]) - max(neededTime[f:l+1])
        return ans
                
