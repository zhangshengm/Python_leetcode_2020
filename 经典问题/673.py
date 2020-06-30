class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        #dp[i]代表以i结尾的最大递增子序列长度
        dp=[1]*len(nums)
        #通往以i结尾的路径条数
        Length=[1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                   if dp[j]+1 > dp[i]:# 代表第一次遇到最长子序列
                        #更新dp[i]
                        dp[i] = 1+dp[j]
                        #路径的次数保持一致 n到1，取n=[1,2,..,多]
                        Length[i] = Length[j]
                   #因为每个下标j代表不同的元素，所以每个Length[j]都是不同的
                   elif dp[j]+1 == dp[i]:# 代表已经遇到过最长子序列
                        Length[i]+=Length[j]
        #先在dp中找到最长路径值，可能有多个，再在Length中根据下标找到每个最大值的路径数目
        t=sum([Length[i] for i in range(len(dp)) if dp[i]==max(dp)])
        return (t) 
        
