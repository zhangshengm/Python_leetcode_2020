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
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        premax=nums[0]
        premin=nums[0]
        for i in range(1,len(nums)):
            #当前值，当前值乘以之前的最大值，当前值乘以之前的最小值
            t=(nums[i],nums[i]*premax,nums[i]*premin)
            curmax=max(t)
            curmin=min(t)
            res=max(res,curmax)
            premax=curmax
            premin=curmin
        return res
    
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            #如果有零元素则重新计算累加和 *1
            #正序最大值nums
            #反序最大值reverse_nums
            nums[i] *= nums[i - 1] or 1
            reverse_nums[i] *= reverse_nums[i - 1] or 1
        return max(nums + reverse_nums)

