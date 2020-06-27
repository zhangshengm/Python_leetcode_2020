class Solution:
    def rob(self, nums: List[int]) -> int:
        

        if not nums:return 0
        if len(nums)==1: return nums[0]

        def findmax(nums):
            #dp[i]代表第i个元素结尾的最大累加值
            if len(nums)==1: return nums[0]
            dp=[0]*(len(nums)+1)
            dp[0]=0
            dp[1]=nums[0]
            dp[2]=max(nums[1],nums[0])
            for i in range(3,len(nums)+1):    
                dp[i]=max(dp[i-2]+nums[i-1],dp[i-1])
            return max(dp)
        return max(findmax(nums[1:]),findmax(nums[:-1]))
