class Solution:
    #O(N2)
    #O(N)
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp=[1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                #满足递增，之前的最大子串长度加1
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
        
