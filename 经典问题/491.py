class Solution:
 

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        s=set()
        def dfs(t,j):
            #长度大于1加入set集合
            if len(t)>1: s.add(t)
            if j>=len(nums): return 
            if not t or t[-1]<=nums[j]:
               dfs(t+(nums[j],),j+1)
            dfs(t,j+1)
        dfs((),0)
        return list(s)
