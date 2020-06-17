class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp=0
        s1=[]
        if not nums: return 
        for i in range(len(nums)):
            temp+=nums[i]
            if temp<0:
               temp=0
            else:
                if not s1 or s1[-1]<temp:
                    s1.append(temp)
        if not s1:
            return max(nums)
        return s1[-1]

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[:]  # 初始化dp数组，dp[i]存储以nums[i]为结尾的子数组的和的最大值
        res = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i], dp[i] + dp[i - 1])  # 更新dp[i]
            res = max(res, dp[i]) # 更新全局最大值
        return res
