class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxn=[nums[0]]
        minn=[nums[0]]  
        for i in range(1,len(nums)):
            #当前值，当前值乘以之前的最大值，当前值乘以之前的最小值
            t=(nums[i],nums[i]*maxn[-1],nums[i]*minn[-1])
            maxn.append(max(t))
            minn.append(min(t))
        return max(maxn)
