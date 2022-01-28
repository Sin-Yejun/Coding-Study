class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def search(root, h):
            if root is None:
                return
            ans.append([root.val, h])
            h += 1
            search(root.left,h)
            search(root.right,h)
        
        ans = []
        search(root,0)
        Max = 0
        for i in range(len(ans)):
            if Max < ans[i][1]:
                Max = ans[i][1]
        arr = [0 for i in range(Max+1)]
        cnt = [0 for i in range(Max+1)]
        
        for i in range(len(ans)):
            arr[ans[i][1]] += ans[i][0]
            cnt[ans[i][1]] += 1
        answer = []    
        for i in range(len(arr)):
            answer.append(float(arr[i])/float(cnt[i]))
            
        return answer
        
        
                
                
        
        
        
